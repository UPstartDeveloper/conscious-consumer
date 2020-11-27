from django.contrib import admin
from conscious_consumer.settings.settings import ADMIN_TITLE
from .models import Goal, Comment

admin.site.site_header = ADMIN_TITLE
admin.site.register(Goal)
admin.site.register(Comment)
