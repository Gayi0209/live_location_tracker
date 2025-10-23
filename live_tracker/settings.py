"""
Django settings for live_tracker project.
...
"""

import os ## <-- MODIFIED: Import os to read environment variables
import dj_database_url ## <-- MODIFIED: Import dj-database-url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
## <-- MODIFIED: Your SECRET_KEY is read from an "environment variable"
## Your hosting provider (like Render/Heroku) will let you set this.
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
## <-- MODIFIED: DEBUG is set to False. If 'RENDER' env var is present, it's False.
## Otherwise, it's True (for local development).
DEBUG = 'RENDER' not in os.environ

## <-- MODIFIED: Add your live website URL here.
## This example is for Render.com's free hosting.
ALLOWED_HOSTS = ['127.0.0.1']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', ## <-- MODIFIED: For static files
    'django.contrib.staticfiles',
    'tracker',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', ## <-- MODIFIED: For static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'live_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'live_tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

## <-- MODIFIED: This now reads a DATABASE_URL environment variable for production
## but falls back to your sqlite3 database for local development.
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# Password validation
# ... (rest of the file is the same) ...


# Internationalization
# ...

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

## <-- MODIFIED: Added STATIC_ROOT and Whitenoise storage
# This is where collectstatic will gather all static files
STATIC_ROOT = BASE_DIR / 'staticfiles'

# This makes sure Whitenoise can serve compressed files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# ...

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
