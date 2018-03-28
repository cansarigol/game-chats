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

    def _games_list_from_name(self, name, order='popularity:desc', count=20, page=1):
        result = {'error': True, 'message': ""}
        if not name:
            result['message']="Parameter not found"
            return result

        if not self.headers['user-key']:
            result['message']="user-key not found"
            return result

        r = requests.get(f'{self.url}/games/?search={name}&fields=id,name,slug,websites,rating,rating_count,cover,genres,summary,first_release_date&limit=20&order=popularity:desc', headers=self.headers)
        games = r.json()
        for game in games:
            if 'genres' in game:
                game['genres_with_name'] = _get_genres_from_ids(self.url, ",".join(map(str, game['genres'])), 'name', self.headers)
            
            if 'websites' in game:
                for website in game['websites']:
                    if website['category'] == 1:
                        website['name']="Official site"
                    elif website['category'] == 5:
                        website['name']="Twitter"
                    elif website['category'] == 6:
                        website['name']="Twitch"
                    elif website['category'] == 9:
                        website['name']="Youtube"
                    elif website['category'] == 13:
                        website['name']="Steam"
                    else:
                        game['websites'].remove(website)
            else:
                game['websites'] = []
                
            if 'slug' in game:
                game_slug = game['slug']    
                game['websites'].append({
                    'category': 1001,
                    'url': f'https://igdb.com/games/{game_slug}',
                    'name': "IGDB site"
                })
        
        return games