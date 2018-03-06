from django.contrib.auth.models import AnonymousUser
import pytest
from ..base import create_request
from home.views import IndexView, LoginView, GamesListView
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

class TestClass:
    def test_manage(self):
        request = create_request(is_post=False, url='/user/manage/', is_anonymous=True)
        response = IndexView.as_view()(request)
        assert response.status_code == 200, "Error"

    def test_logout(self):
        request = create_request(is_post=False, url='/user/manage/', is_anonymous=True)
        response = IndexView.as_view()(request)
        assert response.status_code == 200, "Error"