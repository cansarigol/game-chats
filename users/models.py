from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db import models
from .utils import generate_new_activation_key

class UserManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not name:
            raise ValueError('Users must have a name')

        user = User(
            email=UserManager.normalize_email(email),
            name=name,
            is_active=True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_from_email(self, email):
        user = self.filter(email=email)

        if user:
            return user[0]

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    date_joined = models.DateTimeField(null=True)

    is_accept_agreement = models.BooleanField(default=True)
    is_accept_notify = models.BooleanField(default=False)

    is_sms_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobil']

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(blank=True, null=True)
    first_key = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name

    def save(self):
        self.activation_key = generate_new_activation_key(self.user.email)
        super().save()


    @staticmethod
    def valid_activation_key(user, verify_code):
        return UserProfile.objects.filter(activation_key=verify_code, user=user)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

