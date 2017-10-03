from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from apps.accounts.forms import CreateAccountForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.accounts.forms import ProfileForm
from apps.accounts.models import Profile


def create(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)

        if form.is_valid():
            create_account(form)
    else:
        form = CreateAccountForm()

    return render(request, 'accounts/create.html', {
            'form': form,
            'hide_navlinks': True,
        })

def delete(request):
    return render(request, 'accounts/delete.html', {

    })

@login_required
def profile(request):
    user_id = request.user.id
    user = get_object_or_404(User, id=user_id)
    profile = Profile.objects.filter(user_id=user_id)

    if not profile.exists():
        return redirect('accounts:new_profile')

    return render(request, 'accounts/profile.html', {
        'profile': profile.first(),
        'user': user,
    })


@login_required
def new_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            create_profile(request, form)
    else:
        form = ProfileForm()
    return render(request, 'accounts/profile_new.html', {
            'form': form,
        })


@login_required
def settings(request):
    return render(request, 'accounts/settings.html', {
            'name': request.user.first_name,
        })


# Helper methods
def create_account(postInfo):
    first_name = postInfo.cleaned_data['first_name']
    username = postInfo.cleaned_data['username']
    password = postInfo.cleaned_data['password']
    password2 = postInfo.cleaned_data['password2']
    email = postInfo.cleaned_data['email']

    new_user = User.objects.create_user(username, email, password)
    new_user.first_name = first_name
    new_user.save()


def create_profile(request, profile_data):
    user_id = request.user.id
    birthday = profile_data.cleaned_data['birthday']
    location = profile_data.cleaned_data['location']
    picture = profile_data.cleaned_data['picture']
    next_mountain1 = profile_data.cleaned_data['next_mountain1']
    next_mountain2 = profile_data.cleaned_data['next_mountain2']
    next_mountain3 = profile_data.cleaned_data['next_mountain3']
    next_mountain4 = profile_data.cleaned_data['next_mountain4']
    next_mountain5 = profile_data.cleaned_data['next_mountain5']

    new_profile = Profile.objects.create(
        user_id = user_id,
        birthday = birthday,
        location = location,
        picture = picture,
        next_mountain1 = next_mountain1,
        next_mountain2 = next_mountain2,
        next_mountain3 = next_mountain3,
        next_mountain4 = next_mountain4,
        next_mountain5 = next_mountain5,
    )

    new_profile.save()
