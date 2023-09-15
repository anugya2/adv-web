from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-rr-60h*&j6=c)1snuz-lo8-8j8%_(to7ef&v4&&a1^3%y83k7^"

DEBUG = True

# I wrote this code
INSTALLED_APPS = [
    # "daphne", #uncomment this for newer version of channels    
    'rest_framework',
    "jquery",
    "channels",
    "chat",
    "bootstrap4",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
# end of code I wrote

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "chat_example.urls"

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
            ],
        },
    },
]

# I wrote this code
WSGI_APPLICATION = "chat_example.wsgi.application"
ASGI_APPLICATION = "chat_example.routing.application" # Adding asynchronous application for web socket.
# end of code I wrote

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# I wrote this code
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',    
]
STATIC_URL = "/static/" #template for path of static assets 
MEDIA_ROOT = "images"
MEDIA_URL = "/images/"
# end of code I wrote

CHANNEL_LAYERS = {
    "default" : {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [( "127.0.0.1" , 6379 )]
        },
    },
}


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
