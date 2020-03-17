from django.db import models
from django.urls import reverse
from django.conf import settings


class Profile(models.Model):
    """Inspiration for the mugshot field, as well as the __str__ and
       get_absolute_url method, goes to Travelly source code:
       https://github.com/UPstartDeveloper/fiercely-souvenir/blob/master/travelly/accounts/models.py

    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    mugshot = models.ImageField(upload_to='images/',
                                default='images/user-icon.png',
                                help_text="User profile image")

    def __str__(self):
        '''Return the related User's username.'''
        return f"{self.user.username}'s Profile"

    """
    def get_absolute_url(self):
        '''Returns a fully qualified path for user profile.'''
        path_components = {'pk': self.user.id}
        return reverse('accounts:acct_info', kwargs=path_components)
    """
