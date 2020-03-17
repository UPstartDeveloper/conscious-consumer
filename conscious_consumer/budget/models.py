from django.db import models
from django.conf import settings as dj_conf_settings
import conscious_consumer.settings as cc_settings


class Goal(models.Model):
    title = models.CharField(max_length=cc_settings.LABEL_MAX_LENGTH,
                             unique=True,
                             help_text="Title of the goal.")
    author = models.ForeignKey(dj_conf_settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT,
                               help_text="The user that posted this article.")
    slug = models.CharField(max_length=cc_settings.LABEL_MAX_LENGTH,
                            blank=True, editable=False,
                            help_text=("Unique URL path to access this goal. "
                                       + "Generated by the system."))
    description = models.TextField(help_text="The full details of the goal.")
    created = models.DateTimeField(auto_now_add=True,
                                   help_text=("The date and time this goal was"
                                              + " created. Automatically " +
                                              "generated when the model " +
                                              "saves."))
    modified = models.DateTimeField(auto_now=True,
                                    help_text=("The date and time this goal " +
                                               "was updated. Automatically " +
                                               "generated when the model " +
                                               "updates."))
    achievements = models.IntegerField(help_text=(
        "The number of time periods you have met this goal. Honor system!"
    ))
    fails = models.IntegerField(help_text=(
        "The number of time periods you have missed this goal. Honor system!"
    ))

    def save(self, *args, **kwargs):
        '''Creates a URL safe slug automatically when a new a goal is made.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Goal, self).save(*args, **kwargs)

    def __str__(self):
        '''Return a descriptive name to reference the goal.'''
        return f'{self.title}'

    """
    def get_absolute_url(self):
        '''Returns a fully-qualified path for a goal.'''
        path_components = {'slug': self.slug}
        return reverse('wiki:wiki-details-page', kwargs=path_components)
    """


class Comment(models.Model):
    user = models.OneToOneField(dj_conf_settings.AUTH_USER_MODEL,
                                on_delete=models.PROTECT,
                                help_text="User who wrote the comment.")
    goal = models.ForeignKey(Goal, on_delete=models.PROTECT,
                             help_text="Goal referred to by the comment.")
    headline = models.CharField(max_length=cc_settings.LABEL_MAX_LENGTH,
                                editable=True, help_text=(
                                 "Main gist of the comment."))
    description = models.TextField(help_text="Full description of comment.")
    last_modified = models.DateTimeField(auto_now_add=True, help_text=(
                                         "The date and time this comment" +
                                         " was last edited. Auto-generated."))

    def __str__(self):
        '''Return a descriptive name to reference the comment.'''
        return f"Comment {self.id} for '{self.goal}'"