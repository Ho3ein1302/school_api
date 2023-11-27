from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _

from core.validators import check_phone, check_code_meli


class MyUserManager(UserManager):
    class MyUserManager(UserManager):
        """
            Creating a new user manager for our customized django user.
        """

        def create_superuser(self, username=None, email=None, password=None, **extra_fields):
            extra_fields.setdefault('first_name', 'admin')
            return super().create_superuser(username, email, password, **extra_fields)

        def create_user(self, username=None, email=None, password=None, **extra_fields):
            return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    code_meli = models.IntegerField(
        primary_key=True,
        validators=[check_code_meli],
        verbose_name=_('code_meli')
    )
    phone_number = models.CharField(
        validators=[check_phone],
        verbose_name=_('phone number'),
        db_index=True,
        unique=True
    )
    bio = models.TextField(
        verbose_name=_('bio'),
        blank=True,
        null=True
    )
    objects = MyUserManager()

    def __str__(self):
        return f'{self.last_name} | {self.code_meli}'

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(self, *args, **kwargs)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
