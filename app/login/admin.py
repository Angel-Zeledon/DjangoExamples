
from django.contrib import admin
from login.models import Usuario


@admin.register(Usuario)
class Usuario(admin.ModelAdmin):
    list_display = ['password', 'email', 'name']
