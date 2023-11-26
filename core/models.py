from django.db import models
from django.contrib.gis.db import models as model
from django.utils import timezone
from django.utils.translation import gettext as _

from rest_framework.validators import ValidationError

from .validators import check_landline_number, check_file_extension
from user.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated at'
    )


class School(BaseModel):
    name = models.CharField(
        max_length=300,
        db_index=True,
        verbose_name='name'
    )
    description = models.CharField(
        max_length=1000,
        blank=True, null=True,
        verbose_name='description'
    )
    landline_number = models.CharField(
        max_length=11,
        validators=[check_landline_number]
    )
    address = models.TextField(
        verbose_name='address'
    )
    location = model.GeometryField(
        geography=True,
        verbose_name='location'
    )

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


class HomeRoom(BaseModel):
    school = models.ForeignKey(
        to=School,
        on_delete=models.CASCADE,
        verbose_name=_('school')
    )
    teacher = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='teacher',
        verbose_name=_('teacher')
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name=_('course')
    )
    students = models.ManyToManyField(
        to=User,
        related_name='students',
        verbose_name=_('students')
    )

    def __str__(self):
        return f'{self.school.name} | {self.teacher.username} | {self.course.name}'

    class Meta:
        verbose_name = _('class')
        verbose_name_plural = _('classes')


class News(BaseModel):
    title = models.CharField(
        max_length=300,
        db_index=True,
        verbose_name=_('Title')
    )
    body = models.TextField(
        verbose_name=_('body')
    )
    home_room_id = models.ForeignKey(
        to=HomeRoom,
        on_delete=models.CASCADE,
        verbose_name=_('homeroom')
    )

    def __str__(self):
        return f'{self.title} | {self.home_room_id.__str__()}'

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')


class HomeWork(BaseModel):
    title = models.CharField(
        max_length=400,
        db_index=True,
        verbose_name=_('Title'))
    body = models.TextField(
        verbose_name=_('body')
    )
    attachment = models.FileField(
        upload_to='homework/',
        validators=[check_file_extension],
        null=True,
        blank=True,
        verbose_name=_('attachment')
    )
    homeroom_id = models.ForeignKey(
        to=HomeRoom,
        on_delete=models.CASCADE,
        verbose_name=_('homeroom')
    )
    deadline_time = models.DateField(
        verbose_name=_('deadline time')
    )

    def __str__(self):
        return f'{self.title} | {self.homeroom_id.__str__()}'

    class Meta:
        verbose_name = _('Home work')
        verbose_name_plural = _('home works')


