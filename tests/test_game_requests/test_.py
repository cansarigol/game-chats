import pytest
from django.conf import settings
from game_requests.adapter import BaseAdapter

pytestmark = pytest.mark.django_db

class TestBase:
    def test_adapter(self):
        base_adapter = BaseAdapter()
        r = base_adapter._games_list_from_name('')
        assert isinstance(r, dict), "Json error"
        assert r['error'], "Game name"

        r = base_adapter._games_list_from_name('horizon')
        assert r['error'], r

        settings.IGDB_API_KEY = "4aa780d9f54956d8330470f4cd303d47"
        base_adapter = BaseAdapter()
        r = base_adapter._games_list_from_name('horizon')
        assert 'horizon' in r[0]['name'].lower(), "Name not found on IGDB"
        