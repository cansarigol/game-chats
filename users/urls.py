from django.urls import path
from .views import ManageView

app_name='users'
urlpatterns = [
    path(r'/manage/', ManageView.as_view(), name="manage"),
]