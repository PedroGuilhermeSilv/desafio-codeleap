from ._base import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
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

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEBUG = False

STATIC_URL = "/static/"

STATIC_ROOT = "src/django_project/static"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
