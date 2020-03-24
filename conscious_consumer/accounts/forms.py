from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# credit for subclassing UserCreationForm belongs to
# https://overiq.com/django-1-10/django-creating-users-using-usercreationform/


class SignUpForm(UserCreationForm):
    '''A form to register new users.'''
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1', 'password2']

    def save(self, commit=True):
        '''Initializes fields of the new User instance.'''
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit is True:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
