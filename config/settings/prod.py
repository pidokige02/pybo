from .base import *

import environ

ALLOWED_HOSTS = [
    '3.35.153.92',
    'hobbycoding.site',
    '127.0.0.1',
    '68.183.214.22',
]

STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pybo_v2',
        'USER': 'root',
        'PASSWORD': 'secret123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': '',
#     }
# }
