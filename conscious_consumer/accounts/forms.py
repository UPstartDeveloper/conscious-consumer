from django.contrib.auth.forms import UserCreationForm
from django.conf import settings as dj_conf_settings

# credit for subclassing UserCreationForm belongs to
# https://overiq.com/django-1-10/django-creating-users-using-usercreationform/


class SignUpForm(UserCreationForm):
    '''A form to register new users.'''
    class Meta:
        model = dj_conf_settings.AUTH_USER_MODEL
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
