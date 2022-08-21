"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from decouple import config, Csv
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='')

if config('USE_AZURE_VAULT', default=False, cast=bool):
    SECRET_KEY = SecretClient(vault_url = "https://nickbrett-bem-azvault.vault.azure.net/",
                            credential = DefaultAzureCredential()).get_secret('djangosecret')
else:
    SECRET_KEY = config("SECRET_KEY", default='')

LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'formatters': {
        'file' : {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'filters': [],
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'general.log',
            'formatter' : 'file'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',  # change debug level as appropiate
            'propagate': False,
        },
        'django.security.csrf': {
            'handlers': ['file'],
            'level': 'INFO',  # change debug level as appropiate
            'propagate': False,
        }
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sslserver',
    'webpack_loader',
    'graphene_django',
    'main'
]

GRAPHENE= {
    'SCHEMA': 'webapp.schema.schema'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'request_logging.middleware.LoggingMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_referrer_policy.middleware.ReferrerPolicyMiddleware'
]

REFERRER_POLICY = 'strict-origin-when-cross-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

ROOT_URLCONF = 'webapp.urls'

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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WEBPACK_LOADER = {
  'DEFAULT': {
    'CACHE': not DEBUG,
    'STATS_FILE': os.path.join(BASE_DIR,'webpack-stats.json'),
    'BUNDLE_DIR_NAME' : 'webpack_bundles/',
    'POLL_INTERVAL': 0.1,
    'TIMEOUT': None,
    'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
  }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

USE_TZ=True
