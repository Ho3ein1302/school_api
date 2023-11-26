from django.db import models
from django.contrib.gis.db import models as model

from .validators import check_landline_number


class School(models.Model):
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
