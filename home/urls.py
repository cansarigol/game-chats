from django.urls import path
from .views import IndexView, LoginView, GamesListView, SignupView, ResetPasswordView

app_name='home'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('reset-password/', ResetPasswordView.as_view(), name="reset_password"),
    path('games-list/', GamesListView.as_view(), name="gameslist"),
]