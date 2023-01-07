from django.contrib import admin
from .models import Userpwd

@admin.register(Userpwd)
class UserpwdAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'password')