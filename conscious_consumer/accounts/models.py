from django.db import models
from django.urls import reverse
import django.conf.settings as dj_conf_settings
import conscious_consumer.settings as cc_settings
from store.models import Product


class Profile(models.Model):
    """Inspiration for the mugshot field, as well as the __str__ and
       get_absolute_url method, goes to Travelly source code:
       https://github.com/UPstartDeveloper/fiercely-souvenir/blob/master/travelly/accounts/models.py

    """
    user = models.OneToOneField(dj_conf_settings.AUTH_USER_MODEL,
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


class Interest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                help_text="Related user profile.")
    label = models.CharField(max_length=cc_settings.LABEL_MAX_LENGTH,
                             editable=True, help_text=(
                              "Category of products that would make it easier "
                              + "for this user to keep to their buget goals."
                             ))
    product = models.ForeignKey(Product, on_delete=models.PROTECT,
                                help_text=(
                                 "Related products to be recommended.")
                                )


class Notification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                help_text="Related user profile.")
    label = models.CharField(max_length=cc_settings.LABEL_MAX_LENGTH,
                             editable=True, help_text=(
                              "Message to user about someone reviewing their" +
                              " product for sale, delivery of a bought product"
                              + ", or a comment on their goal by another user."
                             ))
    # ... are more fields needed here? I'm putting this feature on hold for now
