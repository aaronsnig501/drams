from django.contrib import admin
from django import forms
from django.forms import TextInput, CharField
from django.db import models
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdminConfig(UserAdmin):

    model = Account
    search_fields = ("email", "username")
    list_filter = ("email", "username", "is_active", "is_staff")
    ordering = ("-created_on",)
    list_display = ("email", "username", "is_active", "is_staff")

    fieldsets = (
        (None, {"fields": ("email", "username")}),
        ("Permissions", {"fields": ("is_staff", "is_active")})
    )

    add_fieldsets = (
         (None, {
             "classes": ("wide",),
             "fields": (
                "email", "username", "password1", "password2", "is_active", "is_staff"
            )
         })
    )


admin.site.register(Account, AccountAdminConfig)