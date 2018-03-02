from django.urls import path
from .views import ManageView, LogoutView, valid_user

app_name='users'
urlpatterns = [
    path('manage/', ManageView.as_view(), name="manage"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('valid-email/<activation_key>/', valid_user, name="valid_email"),
]