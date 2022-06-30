from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
import datetime 
# import jsonfield
from django.utils.translation import gettext_lazy as _
from numpy import product

from datetime import datetime, timezone


# Create your models here.
class Farmer_registration(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=50)
    farmer_address = models.CharField(max_length=100)
    farmer_phone = models.CharField(max_length=50)
    farmer_email = models.EmailField(max_length=50)
    farmer_password = models.CharField(max_length=50)
    farmer_img = models.CharField(max_length=255)
    account_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(default= datetime.utcnow().replace(tzinfo=timezone.utc) , blank=True)
    class Meta:
        db_table = 'Farmer'



class Otp(models.Model):
    otp = models.CharField(max_length=50, blank=True, null= True)
    email = models.CharField(max_length=50, blank=True, null= True)
    class Meta:
        db_table = 'Otp'

class Products(models.Model):
    product_Id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    product_price = models.CharField(max_length=50)
    product_offer = models.CharField(max_length=50)
    product_brand = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100000)
    product_img = models.CharField(max_length=500)
    stock_size = models.IntegerField(default=1)
    class Meta:
        db_table = 'Products'

class WishList(models.Model):
    wishList_id = models.AutoField(primary_key=True)
    farmer_id = models.ForeignKey(Farmer_registration, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default= datetime.utcnow().replace(tzinfo=timezone.utc) , blank=True)

    class Meta:
        db_table = 'WishList'

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    farmer_id = models.ForeignKey(Farmer_registration, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default= datetime.utcnow().replace(tzinfo=timezone.utc) , blank=True)
    class Meta:
        db_table = 'Cart'




