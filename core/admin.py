from django.contrib import admin

from . import models


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.HomeRoom)
class HomeRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'teacher', 'course']


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'homeroom_id_id', 'created_at', 'updated_at']


@admin.register(models.HomeWork)
class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'homeroom_id_id', 'deadline_time']


@admin.register(models.HomeWorkResponse)
class HomeWorkResponseResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'homework', 'student']
