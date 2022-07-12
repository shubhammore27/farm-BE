from rest_framework import serializers
from farm.models import *


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer_registration
        fields = '__all__'


class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = ['id', 'otp', 'email']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields =  ['product_Id', 'product_name', 'product_category', 'product_price', 'product_offer', 'product_brand', 'product_description', 'product_img', 'stock_size', 'product_added_by_id', 'product_added_by']

class CartSerializerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
        class Meta:
            model = Chat
            fields = '__all__'
