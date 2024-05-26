import os

from ._base import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "my_db"),
        "USER": os.getenv("POSTGRES_USER", "my_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "my_password"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    },
}


ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True
CORS_REPLACE_HTTPS_REFERER = True
CSRF_TRUSTED_ORIGINS = ["http://*", "https://*"]
CORS_ALLOW_HEADERS = [
    "accept",
    "referer",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-sessionid",
    "x-requested-with",
]
CORS_EXPOSE_HEADERS = ["Set-Cookie"]


DEBUG = False

