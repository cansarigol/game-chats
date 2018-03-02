from django import forms
from .base import MyBaseForm, MyBaseModelForm
from users.models import User
from users.validators import validate_password

class LoginForm(MyBaseForm):
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(MyBaseModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators = [validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email' , 'name', 'password', 'confirm_password']

    def clean_confirm_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if not confirm_password == password:
            raise forms.ValidationError("Password doesn't match")

        return confirm_password