from django.urls import path
from .views import ManageView, LogoutView, valid_user, valid_reset_password, ChangePasswordView

app_name='users'
urlpatterns = [
    path('manage/', ManageView.as_view(), name="manage"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('valid-email/<activation_key>/', valid_user, name="valid_email"),
    path('valid-reset-password/<activation_key>/', valid_reset_password, name="valid_reset_password"),
    path('change-password', ChangePasswordView.as_view(), name='change_password')
]