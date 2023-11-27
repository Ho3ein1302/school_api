from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['code_meli', 'username', 'phone_number', 'is_active']
