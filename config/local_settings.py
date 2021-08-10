import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'al897sja2@3:;@3p48a(*+>%$%'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
