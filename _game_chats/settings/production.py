import os
import json
from django.core.exceptions import ImproperlyConfigured
from .base import *

COMPRESS_ENABLED = True


with open(os.path.join(BASE_DIR, "secrets.json")) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

IGDB_API_KEY = get_secret("IGDB_API_KEY")