from django import forms

class BaseForm(object):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in ["mobil", "password", "payment", "amount"]:
                field.widget.attrs['autocomplete'] = 'off'

class MyBaseForm(BaseForm, forms.Form):

    def confirm_login_allowed(self, user):
        if not user:
            raise forms.ValidationError(
                message="",
                code='invalid_login',
            )
        return True

class MyBaseModelForm(BaseForm, forms.ModelForm):
    pass

