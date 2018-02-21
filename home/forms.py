from django import forms
from .base import MyBaseForm

class LoginForm(MyBaseForm):
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
