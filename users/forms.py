
from django import forms
from home.base import MyBaseForm
from users.validators import validate_password

class ChangePasswordForm(MyBaseForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators = [validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_confirm_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if not confirm_password == password:
            raise forms.ValidationError("Password doesn't match")

        return confirm_password