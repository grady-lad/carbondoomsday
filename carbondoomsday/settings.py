"""Project settings."""

import os
from datetime import timedelta

from configurations import Configuration, values
from dj_database_url import config as database_url_parser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class WebPackDevelopment():
    """The development settings for WebPack."""
    WEBPACK_LOADER = {
        "DEFAULT": {
            "BUNDLE_DIR_NAME": "bundles/",
            "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json")
        },
    }


class WebPackProduction():
    """The production settings for WebPack."""
    WEBPACK_LOADER = {
        "DEFAULT": {
            "BUNDLE_DIR_NAME": "dist/",
            "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats-prod.json")
        },
    }


class Base(Configuration):
    """The base configuration for each environment."""
    PROJECT = "carbondoomsday"

    SCHEMA_TITLE = "CarbonDoomsDay Web API"

    DEBUG = values.BooleanValue(False)

    WSGI_APPLICATION = "carbondoomsday.wsgi.application"

    ROOT_URLCONF = "carbondoomsday.urls"

    WSGI_APPLICATION = "carbondoomsday.wsgi.application"

    DATABASES = {"default": database_url_parser()}
    DATABASES['default']['CONN_MAX_AGE'] = 500

    SECRET_KEY = values.SecretValue()

    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "frontend"),
    ]

    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

    INSTALLED_APPS = (
        "carbondoomsday.carbondioxide",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "whitenoise.runserver_nostatic",
        "django.contrib.staticfiles",
        "django_extensions",
        "django_filters",
        "rest_framework",
        "rest_framework_swagger",
        "opbeat.contrib.django",
        "corsheaders",
        "channels",
        "webpack_loader",
    )

    MIDDLEWARE_CLASSES = (
        "opbeat.contrib.django.middleware.OpbeatAPMMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    )

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "carbondioxide", "templates")],
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

    LOGGING = {
        "version": 1,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            }
        },
        "loggers": {
            "carbondoomsday": {
                "handlers": ["console"],
                "level": "DEBUG",
                "propagate": True,
            },
        },
    }

    CELERY_BROKER_URL = values.Value()
    CELERY_RESULT_BACKEND = values.Value()

    LATEST_CO2_URL = (
        "https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv"
    )

    HISTORIC_CO2_URL = (
        "ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/"
        "surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt"
    )

    REST_FRAMEWORK = {
        "DEFAULT_FILTER_BACKENDS": (
            "rest_framework_filters.backends.DjangoFilterBackend",
            "rest_framework.filters.OrderingFilter",
        ),
        "DEFAULT_PAGINATION_CLASS": (
            "rest_framework.pagination.LimitOffsetPagination"
        ),
        "PAGE_SIZE": 50,
    }

    SWAGGER_SETTINGS = {
        "APIS_SORTER": "alpha",
        "DOC_EXPANSION": "list",
        "JSON_EDITOR": True,
        "SHOW_REQUEST_HEADERS": True,
    }

    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    OPBEAT_APP_ID = values.Value()
    OPBEAT_ORGANIZATION_ID = values.Value()
    OPBEAT_SECRET_TOKEN = values.SecretValue()
    OPBEAT = {
        "APP_ID": OPBEAT_APP_ID,
        "ORGANIZATION_ID": OPBEAT_ORGANIZATION_ID,
        "SECRET_TOKEN": OPBEAT_SECRET_TOKEN,
    }

    CELERY_BEAT_SCHEDULE = {
        "scrape-latest-co2-measurements-from-MLO": {
            "task": "carbondoomsday.carbondioxide.tasks.scrape_latest",
            "schedule": timedelta(hours=6)
        }
    }

    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "asgiref.inmemory.ChannelLayer",
            "ROUTING": "carbondoomsday.routing.channel_routing",
        },
    }

    WEBPACK_LOADER = {
        "DEFAULT": {
            "BUNDLE_DIR_NAME": "bundles/",
            "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
        },
    }


class Production(Base, WebPackProduction):
    """The production environment."""
    ENVIRONMENT = "Production"
    ALLOWED_HOSTS = [
        "carbondoomsday.herokuapp.com",
        "api.carbondoomsday.com",
    ]


class Staging(WebPackProduction, Base):
    """The staging environment."""
    ENVIRONMENT = "Staging"
    ALLOWED_HOSTS = [
        "carbondoomsday-test.herokuapp.com"
    ]


class Development(WebPackDevelopment, Base):
    """The development environment."""
    ENVIRONMENT = "Development"
    DEBUG = values.BooleanValue(True)
    CELERY_TASK_ALWAYS_EAGER = values.BooleanValue(True)
    OPBEAT_DISABLE_SEND = values.BooleanValue(True)
    CORS_ORIGIN_ALLOW_ALL = values.BooleanValue(True)
    CORS_ALLOW_CREDENTIALS = values.BooleanValue(False)
