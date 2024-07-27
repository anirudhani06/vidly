from .settings import *

DEBUG = os.getenv("DEBUG", "0") == "1"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")

ENGINE = os.getenv("DATABASE_ENGINE")

if ENGINE != "django.db.backends.sqlite3":
    DATABASES = {
        "default": {
            "ENGINE": ENGINE,
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


STATIC_URL = f"{os.getenv('STATIC_URL','static')}/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, os.getenv("STATIC_URL", "static")),
]


MEDIA_URL = f"{os.getenv('MEDIA_URL','media')}/"
MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv("MEDIA_URL", "media"))
