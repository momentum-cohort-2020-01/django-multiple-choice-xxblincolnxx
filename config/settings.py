import os
from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    USE_S3=(bool, False),
)
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / ...
BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flashcards',
    'storages',

    # Third-party
    'debug_toolbar',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'django_heroku',
    'image_cropping',

    # Project-specific
    'users',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'flashcard-benji',
        'USER': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Custom user model

AUTH_USER_MODEL = 'users.User'

# Debug toolbar config

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# registration redux settings
REGISTRATION_DEFAULT_FROM_EMAIL = True
REGISTRATION_EMAIL_HTML = True
LOGIN_REDIRECT_URL = '/'
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#  amazon web services settings
if env('USE_S3'):
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    DEFAULT_FILE_STORAGE = 'flashcards.storage_backends.MediaStorage'

# REST API settings
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    # ],
    'DEFAULT_PERMISSIONS_CLASSES': {
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    }
}

# imagecrop settings: 
# from easy_thumbnails.conf import Settings as thumbnail_settings
# THUMBNAIL_PROCESSORS = (
#     'image_cropping.thumbnail_processors.crop_corners',
# ) + thumbnail_settings.THUMBNAIL_PROCESSORS

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())