from django.db import models
from django.contrib.gis.db import models as model
from django.utils import timezone
from django.utils.translation import gettext as _

from rest_framework.validators import ValidationError

from .validators import check_landline_number
from user.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')


class School(BaseModel):
    name = models.CharField(max_length=300, db_index=True, verbose_name='name')
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='description')
    landline_number = models.CharField(max_length=11, validators=[check_landline_number])
    address = models.TextField(verbose_name='address')
    location = model.GeometryField(geography=True, verbose_name='location')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'school'
        verbose_name_plural = 'schools'


class Course(BaseModel):
    name = models.CharField(
        max_length=200,
        unique=True,
        db_index=True,
        verbose_name=_('Course name')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
