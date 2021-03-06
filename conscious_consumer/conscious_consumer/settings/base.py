"""
Django settings for conscious_consumer project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from dotenv import load_dotenv
from pathlib import Path

# enables loading of environment variables (from .env file in development)
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv("SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = [
    "localhost",
    "consciousconsumer.herokuapp.com",
    "127.0.0.1",
    "0.0.0.0"
]

# Max length for charfields
LABEL_MAX_LENGTH = 60

# Header for the Admin site
ADMIN_TITLE = "Conscious Consumer Administration"


# Application definition

INSTALLED_APPS = [
    # built-in apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps added in this repo
    "accounts.apps.AccountsConfig",
    "budget.apps.BudgetConfig",
    "store.apps.StoreConfig",
    "api.apps.ApiConfig",
    # third party libraries
    "rest_framework",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "conscious_consumer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "conscious_consumer.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "NAME": "conscious_consumer",
        "ENGINE": "django.db.backends.postgresql",
        "USER": "postgres",
        "PASSWORD": str(os.getenv("DATABASE_PASSWORD")),
        "HOST": "",
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

VALIDATOR_1 = "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
VALIDATOR_2 = "django.contrib.auth.password_validation.MinimumLengthValidator"
VALIDATOR_3 = "django.contrib.auth.password_validation.CommonPasswordValidator"
VALIDATOR_4 = "django.contrib.auth.password_validation.NumericPasswordValidator"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": VALIDATOR_1},
    {"NAME": VALIDATOR_2},
    {"NAME": VALIDATOR_3},
    {"NAME": VALIDATOR_4},
]


# Auth-related Redirects
LOGIN_REDIRECT_URL = LOGOUT_REDIRECT_URL = "landing_page"

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Los_Angeles"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
# where all the static files will go on collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# where to look for static files applied project-wide
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# AWS S3 Settings (Image Uploads)
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# provision PostgreSQL for deployment
db_from_env = dj_database_url.config()
DATABASES["default"].update(db_from_env)

# more on deployment
django_heroku.settings(locals())
