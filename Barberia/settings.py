"""
Django settings for Barberia project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import paypalrestsdk

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ud7u-k3=%!4yc2a&6cs(1m+)6m-^8ueag7d$u5g%4pbmyknv%5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
USE_THOUSAND_SEPARATOR = True

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App.apps.AppConfig',
    'bootstrap5',
    'crispy_forms',
    'crispy_bootstrap5',
    'paypal.standard.ipn',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

X_FRAME_OPTIONS = 'SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Barberia.urls'

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

WSGI_APPLICATION = 'Barberia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_ROOT = os.path.join(BASE_DIR,'')
MEDIA_URL = '/img/'

#desde acá las pruebas de la integración de paypal

PAYPAL_CLIENT_ID = 'AaIb9JHxcdgLD2PA-KmMUoLn1fKWxL1Cl40tdBRcgTGnggzZVpk2X6LJ9pA6G5CHSmhTAR-Xt2GniAtQ'
PAYPAL_CLIENT_SECRET = 'ENhDDiKbB44UGsByR8jc7Dh6izdJGOQE3VB-dm7Xl7pF7U5bBDziZLkpurj6p3lywD6oZ4AjZbCqW27F'
PAYPAL_MODE = 'sandbox'  # Cambiar a 'live' cuando esté listo para producción


paypalrestsdk.configure({
    "mode": "sandbox",  # sandbox o live
    "client_id": 'AaIb9JHxcdgLD2PA-KmMUoLn1fKWxL1Cl40tdBRcgTGnggzZVpk2X6LJ9pA6G5CHSmhTAR-Xt2GniAtQ',
    "client_secret": 'ENhDDiKbB44UGsByR8jc7Dh6izdJGOQE3VB-dm7Xl7pF7U5bBDziZLkpurj6p3lywD6oZ4AjZbCqW27F'
})