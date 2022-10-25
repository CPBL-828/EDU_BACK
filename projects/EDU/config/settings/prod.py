from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '172.30.1.28', '127.0.0.1', '192.168.0.14', ]

DATABASES = {
    'default': {
        'ENGINE': get_secret("DATABASE_ENGINE"),
        'NAME': get_secret("DATABASE_NAME"),
        'USER': get_secret("DATABASE_USER"),
        'PASSWORD': get_secret("DATABASE_PASS"),
        'HOST': get_secret("DATABASE_HOST"),
        'PORT': get_secret("DATABASE_PORT"),
    }
}
