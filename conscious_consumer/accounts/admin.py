from django.contrib import admin
from conscious_consumer.settings import ADMIN_TITLE
from .models import Profile, Interest, Notification

admin.site.site_header = ADMIN_TITLE
admin.site.register(Profile)
admin.site.register(Interest)
admin.site.register(Notification)
