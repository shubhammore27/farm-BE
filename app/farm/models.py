from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
import datetime 
# import jsonfield
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Farmer_registration(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=50)
    farmer_address = models.CharField(max_length=50)
    farmer_phone = models.CharField(max_length=10)
    farmer_email = models.EmailField(max_length=50)
    farmer_password = models.CharField(max_length=50)
    created_at = models.DateTimeField(default= datetime.datetime.now() , blank=True)

    class Meta:
        db_table = 'Farmer'

class Otp(models.Model):
    otp = models.CharField(max_length=50, blank=True, null= True)
    email = models.CharField(max_length=50, blank=True, null= True)

    class Meta:
        db_table = 'Otp'

