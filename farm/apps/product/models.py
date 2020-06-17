from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)
    class Meta:
       abstract = True


class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    address      = models.CharField(max_length=30)
    profile_img  = models.ImageField(upload_to="profile_image/")


class Product(BaseModel):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    product_img = models.ImageField(upload_to="product_image/")
    prize  = models.IntegerField()

    def __str__(self):
        return self.name

class CustomeDetailBill(BaseModel):
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_number = models.CharField(max_length=13)
    total_list = ArrayField(models.CharField(max_length=255), blank=True)
    product_list = ArrayField(models.CharField(max_length=255), blank=True)
    quantity_list = ArrayField(models.CharField(max_length=255), blank=True)
    unit_price_list = ArrayField(models.CharField(max_length=255), blank=True)
    sub_amount  = models.IntegerField()
    total_amount  = models.IntegerField()

    # product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='choice_product')
    # is_activate  = models.BooleanField(default = False)
