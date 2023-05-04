from django.contrib import admin
from .models import User,Group

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "student_card_id", "password", "chat_id", "group_id"]


class UserGroup(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(User, UserAdmin)
admin.site.register(Group, UserGroup)