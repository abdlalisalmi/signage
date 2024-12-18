import os
from pathlib import Path

from .unfold_settings import UNFOLD

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-#(7!")

# Allowed hosts
ALLOWED_HOSTS = [
    host.strip(" ") for host in os.environ.get("ALLOWED_HOSTS", "*").split(",")
]

# Cors headers
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# CSRF settings
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    CSRF_TRUSTED_ORIGINS = [
        origin.strip(" ")
        for origin in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")
    ]

APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    "unfold",  # Unfold is a new theme for Django Admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # Unfold forms
    # "unfold.contrib.inlines",  # optional, if special inlines are needed
    # "unfold.contrib.import_export",  # optional, if django-import-export package is used
    # "unfold.contrib.guardian",  # optional, if django-guardian package is used
    # "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # Third-party apps
    "rest_framework",  # Django REST framework
    "corsheaders",  # Django CORS headers
    # Local apps
    "signage",
    "frontend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # CORS headers middleware
    "corsheaders.middleware.CorsMiddleware",
    # Whitenoise middleware
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("POSTGRES_HOST", "database"),
            "PORT": os.getenv("POSTGRES_PORT", 5432),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Logging settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}] [{levelname:<8}] {name}: {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": (
                "DEBUG"  # if os.environ.get("DJANGO_ENV") == "development" else "INFO"
            ),
            "class": "logging.StreamHandler",
            "formatter": (
                "verbose"  # if os.environ.get("DJANGO_ENV") == "development" else "simple"
            ),
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",  # if os.environ.get("DJANGO_ENV") == "development" else "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": (
                "INFO"  # if os.environ.get("DJANGO_ENV") == "development" else "INFO"
            ),
            "propagate": False,
        },
        # "django.request": {
        #     "handlers": ["console"],
        #     "level": "ERROR",
        #     "propagate": False,
        # },
        # You can add additional loggers here if needed
    },
}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Casablanca"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
# Additional directories where Django will look for static files
STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "styles",
]
STATIC_DIRS = [BASE_DIR / "static", BASE_DIR / "frontend" / "styles"]
STATIC_ROOT = BASE_DIR / "static"

# MEDIA_URL = "media/" if not DEBUG else "http://localhost:8000/media/"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
