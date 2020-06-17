# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Product, User, CustomeDetailBill

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
   list_display = ("name","quantity")

class UserAdmin(admin.ModelAdmin):
   list_display = ("username","email")

class CustomeDetailBillAdmin(admin.ModelAdmin):
   list_display = ("customer_name","customer_address","product_list","unit_price_list","total_amount")

admin.site.register(Product, ProductAdmin)
admin.site.register(CustomeDetailBill, CustomeDetailBillAdmin)
admin.site.register(User, UserAdmin)
