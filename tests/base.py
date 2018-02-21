from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.test import RequestFactory
from mixer.backend.django import mixer
import pytest


def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


def setup_view(view, request, *args, **kwargs):
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view

def get_response_reason(response, request):
    if isinstance(response, TemplateResponse):
        return response.context_data['form'].errors

    if isinstance(response, HttpResponse):
        return list(request._messages)[0].message

    return response

def create_request(is_post, url, data=None, is_anonymous=None, **kwargs):
    user = AnonymousUser()
    if not is_anonymous:
        user = mixer.blend('users.User')
        user.username = "ertugrulsarigol@gmail.com"
        user.set_password('123')
        for key, value in kwargs:
            setattr(user, key, value)
        user.save()

    factory = RequestFactory()
    request = factory.post(url, data) if is_post else factory.get(url)
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)
    request.user = user
    request = add_middleware_to_request(request, SessionMiddleware)
    request.session.save()

    return request