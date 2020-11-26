from .settings import *

# reset the variables for the CapRover environment
DEBUG = True

SECRET_KEY='odeoe_4^kfoef66D%/?$cgr3)qghsfogqy#6b'

DATABASES = {
    'default': {
        'NAME': 'postgres',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
