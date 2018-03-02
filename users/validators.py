from django.forms import ValidationError

def validate_password(value):
    if not len(value)>=6:
        raise ValidationError(message="Password must 6 characters at least")

        