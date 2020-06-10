from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


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
    customer_name = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=20)
    total_price = models.IntegerField()
    customer_number = models.CharField(max_length=13)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='choice_product')
    select_prod_quantity = models.IntegerField()
    is_activate  = models.BooleanField(default = False)
