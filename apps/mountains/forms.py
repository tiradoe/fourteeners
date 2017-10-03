import time
from django import forms
from apps.mountains.models import Climb

class AddClimbForm(forms.ModelForm):

    class Meta:
        model = Climb
        fields = [
                    'start_date',
                    'start_time',
                    'summit_date',
                    'summit_time',
                    'finish_date',
                    'finish_time',
                    'total_distance',
                    'notes',
                ]

        widgets = {
            'start_date': forms.DateInput(format=('%d %B, %Y')),
            'summit_date': forms.DateInput(format=('%d %B, %Y')),
            'finish_date': forms.DateInput(format=('%d %B, %Y')),
            'start_time': forms.TimeInput(format=('%I:%M %p')),
            'summit_time': forms.TimeInput(format=('%I:%M %p')),
            'finish_time': forms.TimeInput(format=('%I:%M %p')),
        }


    def __init__(self, *args, **kwargs):
        super(AddClimbForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update({'class' : 'datepicker', 'placeholder' : 'Start Date'})
        self.fields['summit_date'].widget.attrs.update({'class' : 'datepicker', 'placeholder' : 'Summit Date'})
        self.fields['finish_date'].widget.attrs.update({'class' : 'datepicker', 'placeholder' : 'Finish Date'})
        self.fields['start_time'].widget.attrs.update({'class' : 'timepicker', 'placeholder' : 'Start Time'})
        self.fields['summit_time'].widget.attrs.update({'class' : 'timepicker', 'placeholder' : 'Summit Time'})
        self.fields['finish_time'].widget.attrs.update({'class' : 'timepicker', 'placeholder' : 'Finish Time'})
        self.fields['total_distance'].widget.attrs.update({'placeholder' : 'Total Distance'})
