from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '43.201.64.65', '15.164.226.182']

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
