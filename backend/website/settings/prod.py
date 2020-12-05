from .base import *

import os

# Secret Key
SECRET_KEY = os.urandom(40)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# Temp database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}