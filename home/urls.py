from django.urls import path
from .views import IndexView, LoginView, GamesListView

app_name='home'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('games-list/', GamesListView.as_view(), name="gameslist"),
]