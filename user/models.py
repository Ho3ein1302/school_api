from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _

from core.validators import check_phone, check_code_meli


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

    def __str__(self):
        return f'{self.last_name} | {self.code_meli}'

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(self, *args, **kwargs)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
