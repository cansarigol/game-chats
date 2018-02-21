from django.contrib.auth.models import AnonymousUser
import pytest
from ..base import create_request
from home.views import IndexView, LoginView
from mixer.backend.django import mixer
from mock import patch

pytestmark = pytest.mark.django_db

class TestBase:
    def test_index(self):
        request = create_request(is_post=False, url='', is_anonymous=True)
        response = IndexView.as_view()(request)
        assert response.status_code == 200, "Error"

    def test_login_view(self):
        request = create_request(is_post=False, url='', is_anonymous=False)
        response = LoginView.as_view()(request)
        assert response.status_code == 302, "Should have redirected"

        request = create_request(is_post=False, url='/login/', is_anonymous=True)
        response = LoginView.as_view()(request)
        assert response.status_code == 200, "Error"


    #@patch("home.views.send_mail", return_value=True)
    #def test_validpassword_post(self, mock_send_mail):
    #    post_url = "sign-up"
    #    assert True
