
from .base import *

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions'
    ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

