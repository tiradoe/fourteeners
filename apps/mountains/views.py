import time
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.mountains.models import Mountain, Climb, Weather
from apps.mountains.forms import AddClimbForm

@login_required
def list(request):
    template_name = 'mountains/list.html'

    mountains = Mountain.objects.all()

    return render(request, template_name, {
        "mountains": mountains,
        "user_id": request.user.id
    })


@login_required
def new(request, peak):
    template_name = 'mountains/new.html'
    mountain = get_object_or_404(Mountain, id=peak)
    weather_data = weather_check(Weather.objects.filter(mountain_id=peak))

    if request.method == 'POST':
        post_copy = request.POST.copy()
        post = update_new_data_for_db(post_copy)

        form = AddClimbForm(post)

        if form.is_valid():
            add_climb(request, form, mountain)
            return redirect('mountains:list')

    else:
        form = AddClimbForm()


    return render(request, template_name, {
        "form": form,
        "name": mountain.name,
        "mountain_id": peak,
        "weather": weather_data,
    })


@login_required
def edit(request, peak):
    template_name = 'mountains/edit.html'
    FormSet = modelformset_factory(Climb, form=AddClimbForm, extra=0)

    mountain = get_object_or_404(Mountain, id=peak)
    climbs = Climb.objects.filter(climber_id=request.user.id, mountain=mountain.name)
    weather_data = weather_check(Weather.objects.filter(mountain_id=peak))
    user_climbs = None

    if not climbs.exists():
        return redirect('mountains:new', peak=peak)

    if request.method == 'POST':
        post_copy = request.POST.copy()
        formset = FormSet(post_copy)

        for form in formset:
            update_edited_data_for_db(form)

        if formset.is_valid():
            edit_climb(request, formset)
            return redirect('mountains:list')
        else:
            print('nope')

    else:
        paginator = Paginator(climbs, 1)
        page = request.GET.get('page')

        try:
            user_climbs = paginator.page(page)
        except PageNotAnInteger:
            user_climbs = paginator.page(1)
        except EmptyPage:
            user_climbs = paginator.page(paginator.num_pages)

        page_query = climbs.filter(id__in=[climb.id for climb in user_climbs])
        formset = FormSet(queryset=page_query)

    return render(request, template_name, {
        "formset": formset,
        "name": mountain.name,
        "mountain_id": peak,
        "climbs": user_climbs,
        "weather": weather_data,
        },
        context_instance=RequestContext(request)
    )


def weather(request, peak):
    mountain = get_object_or_404(Mountain, id=peak)
    template_name = 'mountains/weather.html'

    weather_data = get_object_or_404(Weather, mountain_id=peak)

    return render(request, template_name, {
        "mountain": mountain,
        "weather": weather_data,
        }
    )


# Helper methods

def add_climb(request, form, mountain):
    climber_id = request.user.id
    mountain = mountain.name
    start_date = form.cleaned_data['start_date']
    start_time = form.cleaned_data['start_time']
    summit_date = form.cleaned_data['summit_date']
    summit_time = form.cleaned_data['summit_time']
    finish_date = form.cleaned_data['finish_date']
    finish_time = form.cleaned_data['finish_time']
    total_distance = form.cleaned_data['total_distance']
    notes = form.cleaned_data['notes']

    new_climb = Climb.objects.create(
        climber_id = climber_id,
        mountain = mountain,
        start_date = start_date,
        start_time = start_time,
        summit_date = summit_date,
        summit_time = summit_time,
        finish_date = finish_date,
        finish_time = finish_time,
        total_distance = total_distance,
        notes = notes
    )

    new_climb.save()


def edit_climb(request, formset):
    for form in formset:
        start_date = form.cleaned_data['start_date']
        start_time = form.cleaned_data['start_time']
        summit_date = form.cleaned_data['summit_date']
        summit_time = form.cleaned_data['summit_time']
        finish_date = form.cleaned_data['finish_date']
        finish_time = form.cleaned_data['finish_time']
        total_distance = form.cleaned_data['total_distance']
        notes = form.cleaned_data['notes']

        form.save()


class ClimbDelete(DeleteView):
    model = Climb
    success_url = reverse_lazy('mountains') # This is where this view will
                                            # redirect the user
    template_name = 'delete_climb.html'


def weather_check(weather_data):
    if not weather_data:
        weather_data = ""
    else:
        weather_data = weather_data[0]

    return weather_data

def update_new_data_for_db(post):

    dates = {
        'start_date': post['start_date'],
        'summit_date': post['summit_date'],
        'finish_date': post['finish_date'],
    }

    times = {
        'start_time': post['start_time'],
        'summit_time': post['summit_time'],
        'finish_time': post['finish_time'],
    }

    for key, form_date in dates.items():
        if form_date == '':
            continue

        formatted_date = time.strptime(form_date, "%d %B, %Y")
        new_date = time.strftime("%Y-%m-%d", formatted_date)
        post[key] = new_date

    for key, form_time in times.items():
        if form_time == '':
            continue

        formatted_time = time.strptime(form_time, "%I:%M %p")
        new_time = time.strftime("%I:%M:%S", formatted_time)
        post[key] = new_time

    return post


def update_edited_data_for_db(form):
    """Loops thorough forms and changes date/time format from
       what the user sees to what the database wants.  Keys
       are different from the new climbs so that method can't be reused"""

    dates = {}
    times = {}

    for field in form.data:
        if 'start_date' in field:
            dates[field] = form.data[field]
        if 'summit_date' in field:
            dates[field] = form.data[field]
        if 'finish_date' in field:
            dates[field] = form.data[field]

        if 'start_time' in field:
            times[field] = form.data[field]
        if 'summit_time' in field:
            times[field] = form.data[field]
        if 'finish_time' in field:
            times[field] = form.data[field]

    for key, form_date in dates.items():
        if form_date == '':
            continue

        formatted_date = time.strptime(form_date, "%d %B, %Y")
        new_date = time.strftime("%Y-%m-%d", formatted_date)
        form.data[key] = new_date

    for key, form_time in times.items():
        if form_time == '':
            continue

        formatted_time = time.strptime(form_time, "%I:%M %p")
        new_time = time.strftime("%I:%M:%S", formatted_time)
        form.data[key] = new_time

    return form.data
