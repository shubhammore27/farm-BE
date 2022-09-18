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

class WishlistMapping(ModelForm):
    class Meta:
        model = WishList
        fields =  "__all__"

class CartMapping(ModelForm):
    class Meta:
        model = Cart
        fields =  "__all__"

class ChatMapping(ModelForm):
    class Meta:
        model = Chat
        fields =  "__all__"

class PurchesMapping(ModelForm):
    class Meta:
        model = Purches
        fields =  "__all__"



