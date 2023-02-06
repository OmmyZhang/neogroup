"""
Django settings for neogroup project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9zl*vy7c=q%-!onjs)+@%+9qgyhbbh--+7vf2krzaixlo+dubt"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = ['https://*.github.dev', 'http://127.0.0.1:8000',]

# Application definition

INSTALLED_APPS = [
    "maintenance_mode",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_sass",
    "tz_detect",
    "markdownx",
    "easy_thumbnails",
    "user_messages",
    "mastodon",
    "common",
    "users",
    "group",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "tz_detect.middleware.TimezoneMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
]

ROOT_URLCONF = "neogroup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "neogroup.context_processors.site_info",
            ],
        },
    },
]

WSGI_APPLICATION = "neogroup.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "OPTIONS": {
            "timeout": 20,
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# user upload files
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
GROUP_ICON_MEDIA_ROOT = 'group_icon/'

THUMBNAIL_ALIASES = {
    "": {
        "normal": {
            "size": (200, 200),
            "crop": "scale",
            "autocrop": True,
        },
        "group": {
            "size": (64, 64),
            "crop": "scale",
            "autocrop": True,
        },
        "avatar": {
            "size": (64, 64),
            "crop": "scale",
            "autocrop": True,
        },
    },
}

AUTH_USER_MODEL = "users.User"
AUTHENTICATION_BACKENDS = [
    "mastodon.auth.OAuth2Backend",
]
SILENCED_SYSTEM_CHECKS = [
    "auth.W004",  # User.username is non-unique
    "admin.E404",  # Required by django-user-messages
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_INFO = {
    "site_name": "NeoGroup",
    "support_link": "https://github.com/0xasahi/neogroup/issues",
    "social_link": "",
    "donation_link": "",
    "version_hash": None,
    "settings_module": os.getenv("DJANGO_SETTINGS_MODULE"),
    "sentry_dsn": None,
    "google_analytics_id": "",
    "repo_link": "",
    "matrix_link": "",
}

# Mastodon configs
CLIENT_NAME = os.environ.get("APP_NAME", "NeoGroup")
SITE_INFO["site_name"] = os.environ.get("APP_NAME", "NeoGroup")
APP_WEBSITE = os.environ.get("APP_URL", "https://neogrp.club")
REDIRECT_URIS = APP_WEBSITE + "/users/OAuth2_login/"

# Timeout of requests to Mastodon, in seconds
MASTODON_TIMEOUT = 30

# Allow user to login via any Mastodon/Pleroma sites
MASTODON_ALLOW_ANY_SITE = True

MASTODON_CLIENT_SCOPE = "read write follow"
# use the following if it's a new site
# MASTODON_CLIENT_SCOPE = 'read:accounts read:follows read:search read:blocks read:mutes write:statuses write:media'

MASTODON_LEGACY_CLIENT_SCOPE = "read write follow"

# Tags for toots posted from this site
MASTODON_TAGS = "#NeoGroup"

LOGIN_URL = "/users/login/"

MAINTENANCE_MODE = False
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True
MAINTENANCE_MODE_IGNORE_SUPERUSER = True
MAINTENANCE_MODE_IGNORE_ANONYMOUS_USER = True
MAINTENANCE_MODE_IGNORE_URLS = (r"^/users/connect/", r"^/users/OAuth2_login/")

REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")

RQ_QUEUES = {
    "mastodon": {
        "HOST": REDIS_HOST,
        "PORT": 6379,
        "DB": 0,
        "DEFAULT_TIMEOUT": -1,
    },
    "export": {
        "HOST": REDIS_HOST,
        "PORT": 6379,
        "DB": 0,
        "DEFAULT_TIMEOUT": -1,
    },
    "import": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
        "DEFAULT_TIMEOUT": -1,
    },
    "fetch": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
        "DEFAULT_TIMEOUT": -1,
    },
    "crawl": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
        "DEFAULT_TIMEOUT": -1,
    },
    "doufen": {
        "HOST": REDIS_HOST,
        "PORT": 6379,
        "DB": 0,
        "DEFAULT_TIMEOUT": -1,
    },
}

RQ_SHOW_ADMIN_LINK = True

try:
    from neogroup.local_settings import *
except ImportError:
    pass