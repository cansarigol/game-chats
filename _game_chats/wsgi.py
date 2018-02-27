import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_game_chats.settings.staging")
application = get_wsgi_application()
