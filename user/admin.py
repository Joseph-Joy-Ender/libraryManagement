from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BookUser


# Register your models here.

@admin.register(BookUser)
class Admin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )
