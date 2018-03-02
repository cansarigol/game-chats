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

# EMAIL STUFF
EMAIL_HOST = get_secret("EMAIL_HOST", "test_secrets.json")
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER", "test_secrets.json")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD", "test_secrets.json")
EMAIL_PORT = get_secret("EMAIL_PORT", "test_secrets.json")
EMAIL_USE_SSL = get_secret("EMAIL_USE_SSL", "test_secrets.json")
DEFAULT_FROM_EMAIL = get_secret("DEFAULT_FROM_EMAIL", "test_secrets.json")
SERVER_EMAIL = get_secret("SERVER_EMAIL", "test_secrets.json")