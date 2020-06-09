from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    address      = models.CharField(max_length=30)
    profile_img  = models.ImageField(upload_to="profile_image/")





# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)
    class Meta:
       abstract = True



class Product(BaseModel):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    product_img = models.ImageField(upload_to="product_image/")
    prize  = models.IntegerField()

    def __str__(self):
        return self.name