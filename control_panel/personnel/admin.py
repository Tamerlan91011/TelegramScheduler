from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "telegram_tag"]

admin.site.register(User, UserAdmin)