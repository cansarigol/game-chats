import os
import json
from django.conf import settings

def _get_secrets(file_name):
    with open(os.path.join(settings.BASE_DIR, file_name)) as f:
        return json.loads(f.read())

def get_secret(setting, file_name):
    secrets = _get_secrets(file_name)
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)