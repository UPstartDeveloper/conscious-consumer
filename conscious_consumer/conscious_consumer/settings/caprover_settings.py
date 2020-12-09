import os

from .settings import *

# reset the variables for the CapRover environment
DEBUG = True

DATABASES = {
    "default": {
        "NAME": os.getenv("POSTGRES_DB", "postgres"),
        "ENGINE": "django.db.backends.postgresql",
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.getenv(
            "POSTGRES_HOST", "db"
        ),  # depends on what your PostgreSQL app is called
        "PORT": 5432,
    }
}

ALLOWED_HOSTS.append(
     "conscious-consumer-app.dev.zainraza.me",  # for devs using in prod
)
