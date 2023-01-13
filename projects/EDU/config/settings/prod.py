from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '43.201.64.65', '52.78.111.175']

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
