import requests
from django.conf import settings

def _get_genres_from_ids(url, ids, fields, headers):
    r = requests.get(f'{url}/genres/{ids}/?fields={fields}', headers=headers)
    return r.json()


class BaseAdapter(object):
    def __init__(self):
        self.url = f"{settings.IGDB_API_URL}"
        self.headers = {
            'user-key': settings.IGDB_API_KEY,
            'Accept': 'application/json'
        }

    

    def _games_list_from_name(self, name, count=20, page=1):
        result = {'error': True, 'message': ""}
        if not name:
            result['message']="Parameter not found"
            return result

        if not self.headers['user-key']:
            result['message']="user-key not found"
            return result

        
        fields = "id,name,slug,websites,rating,rating_count,cover,genres,summary,first_release_date"
        r = requests.get(f'{self.url}/games/?search={name}&fields={fields}&limit={count}', headers=self.headers)
        games = r.json()
        for game in games:
            if 'genres' in game:
                game['genres_with_name'] = _get_genres_from_ids(self.url, ",".join(map(str, game['genres'])), 'name', self.headers)
            
            if 'slug' in game:
                game_slug = game['slug']
                if not 'websites' in game:
                    game['websites'] = []
                game['websites'].append({
                    'category': 1001,
                    'url': f'https://igdb.com/games/{game_slug}'
                })
        
        return games