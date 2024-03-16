from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-s%!8wyny2xnks@4d-k$_ght3nrsidf8^a6*#q=_%i@_^h=isaw"


DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
