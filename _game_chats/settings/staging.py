from .base import *
from . import get_secret
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': "db",
        'PORT': 5432,
    }
}

IGDB_API_KEY = get_secret("IGDB_API_KEY", "test_secrets.json")

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INTERNAL_IPS = ['127.0.0.1']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'logs','error.log'),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        }
    },
}