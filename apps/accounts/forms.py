from django import forms
from django.contrib.auth.models import User
from apps.accounts.models import Profile

class CreateAccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=30, required=True, label="Password (again)", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['first_name'].widget.attrs.update({'class' : 'account-field'})
        self.fields['username'].widget.attrs.update({'class' : 'account-field'})
        self.fields['password'].widget.attrs.update({'class' : 'account-field'})
        self.fields['password2'].widget.attrs.update({'class' : 'account-field'})
        self.fields['email'].widget.attrs.update({'class' : 'account-field'})

    def clean(self):
        super(CreateAccountForm, self).clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Passwords do not match")

        return self.cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
                    'birthday', 
                    'location', 
                    'picture', 
                    'next_mountain1', 
                    'next_mountain2', 
                    'next_mountain3',
                    'next_mountain4',
                    'next_mountain5',
                ]
