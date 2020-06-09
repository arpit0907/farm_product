# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Product, User

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
   list_display = ("name","quantity")

class UserAdmin(admin.ModelAdmin):
   list_display = ("username","email")

admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)