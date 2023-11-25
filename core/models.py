from django.db import models
from django.contrib.gis.db import models as model


class School(models.Model):
    name = models.CharField(max_length=300, db_index=True, verbose_name='name')
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='description')
    address = models.TextField(verbose_name='address')
    location = model.GeometryField(geography=True, verbose_name='location')

    class Meta:
        verbose_name = 'school'
        verbose_name_plural = 'schools'
