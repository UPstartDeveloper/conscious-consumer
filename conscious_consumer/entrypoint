#!/bin/bash

# tell Django which settings to use 
export DJANGO_SETTINGS_MODULE=conscious_consumer.settings.caprover_settings
# python manage.py commands
python manage.py migrate --noinput

python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8000