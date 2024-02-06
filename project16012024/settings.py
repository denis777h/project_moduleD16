"""
Django settings for project16012024 project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
LOGGING_CONFIG = None

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m!wn&^-ttazj8zde0%s_jco(*+ebhf3d=)!o*^ypsy@zx!uz2m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25


SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'news',
    'news.apps',
    'bootstrap4',
    'django_apscheduler',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_filters',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'project16012024.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'project16012024.wsgi.application'

ADMINS = [
    ('admin', 'support@gmail.com'),
]
SERVER_EMAIL = 'bbs@yandex.ru'
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'console_debug_info': {
            'format': '{astime} {levelname} {message}',
            'style': '{',
        },
        'console_warning': {
            'format': '{astime} {levelname} {message} {pathname}',
            'style': '{',
        },
        'console_error_critical': {
            'format': '{sctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'file_general_log': {
            'format': '{astime} {levelname} {module} {message}',
            'style': '{',
        },
        'file_errors_log': {
            'format': '{astime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'file_security_log': {
            'format': '{atime} {levelname} {module} {message}',
            'style': '{',
        },
        'mail_errors_log': {
            'format': '{astime} {levelname} {message} {pathname}',
            'style': '{',
        }

    },
    'handlers': {
        'console_debug_info': {
            'level': 'DEBUG',
            'filters': ['require_debug_true', 'debug_info_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_debug_info'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true', 'warning_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning'
        },
        'console_error_critical': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_error_critical'
        },
        'file_general_log': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'Logging/general.log',
            'formatter': 'file_general_log'
        },
        'file_errors_log': {
            'class': 'logging.FileHandler',
            'filename': 'Logging/errors.log',
            'formatter': 'file_errors_log'
        },
        'file_security_log': {
            'class': 'logging.FileHandler',
            'filename': 'Logging/security.log',
            'formatter': 'file_security_log'
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'mail_errors_log'
        }
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console_debug_info', 'console_warning', 'console_error_critical', 'file_general_log'],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            'propagate': True
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['file_errors_log', 'mail_admins'],
        },
        'django.server': {
            'level': 'ERROR',
            'handlers': ['file_errors_log', 'mail_admins'],
        },
        'django.template': {
            'level': 'ERROR',
            'handlers': ['file_errors_log'],
        },
        'django.db_backends': {
            'level': 'ERROR',
            'handlers': ['file_errors_log'],
        },
        'django.security': {
            'level': 'DEBUG',
            'handlers': ['file_security_log'],
        },
    }
}







AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',


    'allauth.account.auth_backends.AuthenticationBackend',
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 90

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'