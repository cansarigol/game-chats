from django.urls import path
from .views import ManageView

app_name='users'
urlpatterns = [
    path('manage/', ManageView.as_view(), name="manage"),
]