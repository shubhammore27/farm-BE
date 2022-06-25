from pyexpat import model
from django.forms import ModelForm
from farm.models import *
from django import forms

class Farmer_registration_mapping(ModelForm):
    class Meta:
        model = Farmer_registration
        fields = "__all__"


class OtpMapping(ModelForm):
    class Meta:
        model = Otp
        fields = "__all__"

class Add_product_mapping(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
