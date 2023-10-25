"""
Django settings for nzirani project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from google.oauth2 import service_account
from pathlib import Path
from datetime import timedelta
import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = 1  # make sure SITE_ID is set


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "django-insecure-*zv($h-u1^b2cjxif95=d+)^p#18!d&e-s+s9j@pou%1rf(v)0"
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-*zv($h-us8^2cjxif95=d+)^p#16!d&e-s+s9j@pou273f(v)0')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = os.environ.get('DEBUG', 'False')


GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')


ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'accounts',
    'posts',
    # django-storages[google]
    'storages',
    # for api authentication
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'corsheaders',
    # ...
    "django.contrib.sites",  # make sure 'django.contrib.sites' is installed
    "allauth",
    "allauth.account",
    "allauth.socialaccount",  # add if you want social authentication
    # ... django rest auth
    "dj_rest_auth",
    "dj_rest_auth.registration",
]


MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # ...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nzirani.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'nzirani.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#  integratation of Docker for PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        #'HOST': '/cloudsql/exemplary-proxy-354510:us-central1:nzirani-postgresql',
        'HOST': os.getenv('DATABASE_HOST', 'db'),
        'NAME': os.getenv('DATABASE_NAME', 'your-db-name'),
        'USER': os.getenv('DATABASE_USER', 'your-db-user'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'your-db-password'),
        'PORT': os.getenv("DATABASE_PORT", 5432),
    }
}


# Google Cloud Storage Configurations
GS_BUCKET_NAME = os.environ.get('GS_BUCKET_NAME')
credential_path = os.environ.get('GS_CREDENTIALS_PATH')
if credential_path:
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(credential_path)
else:
    print("GS_CREDENTIALS not set. Google Cloud Services will not be available.")
DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE', 'storages.backends.gcloud.GoogleCloudStorage')
STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE', 'storages.backends.gcloud.GoogleCloudStorage')
GS_PROJECT_ID = os.environ.get('GS_PROJECT_ID')

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [
        'https://api.nzirani.com',
        'https://image-tmak-txbxua333q-uc.a.run.app',
        'https://t-mak.org',
    ]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "complexsigningkey",  # generate a key and replace me
    "ALGORITHM": "HS512",
}

# turn off the email verification functionality
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

