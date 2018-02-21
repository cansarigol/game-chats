import requests
from django.conf import settings

class BaseAdapter(object):
    def __init__(self):
        self.url = f"{settings.IGDB_API_URL}"
        self.headers = {
            'user-key': settings.IGDB_API_KEY,
            'Accept': 'application/json'
        }

    def _games_list_from_name(self, name, count=10, page=1):
        result = {'error': True, 'message': ""}
        if not name:
            result['message']="Parameter not found"
            return result

        if not self.headers['user-key']:
            result['message']="user-key not found"
            return result

        
        fields = "id,name,popularity,rating,rating_count,cover,genres"
        r = requests.get(f'{self.url}/games/?search={name}&fields={fields}&limit={count}', headers=self.headers)
        
        return r.json()