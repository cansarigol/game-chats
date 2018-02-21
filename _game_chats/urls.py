from django.urls import include, path

urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('user/', include('users.urls', namespace="users"))
]
