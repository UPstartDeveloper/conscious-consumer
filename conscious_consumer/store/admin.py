from django.contrib import admin
from .models import Product
from conscious_consumer.settings import ADMIN_TITLE

admin.site.site_header = ADMIN_TITLE
admin.site.register(Product)