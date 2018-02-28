from django.urls import include, path
from django.conf import settings
urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('user/', include('users.urls', namespace="users"))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))