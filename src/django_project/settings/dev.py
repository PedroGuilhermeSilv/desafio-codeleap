from ._base import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    },
}

ALLOWED_HOSTS = ["*"]


DEBUG = True

STATIC_URL = "/static/"

STATIC_ROOT = "src/django_project/static"

STATICFILES_DIRS = [
    BASE_DIR / "static",  # noqa: F405
]
