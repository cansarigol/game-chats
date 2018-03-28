from django.conf import settings

class ApiKeyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        request.api_key = settings.IGDB_API_KEY
        request.api_url = settings.IGDB_API_URL
        response = self.get_response(request)
        return response