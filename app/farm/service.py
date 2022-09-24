import json
import farm
from farm.models import *
from farm.forms import *
from farm.serializer import *
from rest_framework import status
from .emailService import *
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
import random
from django.shortcuts import get_object_or_404


def farmer_registration(req):
    try:
        print(req)
        fd = Farmer_registration_mapping(req)
        print(fd.is_valid())
        print(fd)
        if fd.is_valid():
            is_exists = Farmer_registration.objects.filter(farmer_email=req['farmer_email']).exists()
            if not is_exists:
                fd.save()
                return {'message': 'Registration Successful.', 'status': status.HTTP_200_OK}
            else:
                return {'message': 'Registration Failed, User Already Registered.', 'status': status.HTTP_409_CONFLICT}
        else:
            print(fd.errors())
    except Exception as e:
        print(e)
        return {'message': 'Registration Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def auth(req):
    try:
        res = Auth.objects.filter(id=req['id'])
        if res.count() > 0:
            return {'data': res.values_list('auth') , 'status': status.HTTP_200_OK}
        else:
            return {'message': 'Request Failed.', 'status': status.HTTP_409_CONFLICT}
    except Exception as e:
        print(e)
        return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def getFarmerDetails(req):
    try:
        res = Farmer_registration.objects.filter(farmer_id = req['farmer_id'])
        res = FarmerSerializer(res, many=True)
        if len(res.data) > 0:
            return {'data':res.data, 'status': status.HTTP_200_OK}
        else:
            return {'message':'No records found.', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print(e)
        return {'message': 'Request Failed', 'status': status.HTTP_400_BAD_REQUEST}

def updateProfile(req):
    try:
        get_object_or_404(Farmer_registration, farmer_id=req['farmer_id'])
        res = Farmer_registration.objects.filter(farmer_id=req['farmer_id']).update(
            farmer_name=  req['farmer_name'],
            farmer_address= req['farmer_address'],
            farmer_phone= req['farmer_phone'],
            farmer_email= req['farmer_email'],
            farmer_password= req['farmer_password'],
            farmer_img= req['farmer_img'])
        return {'message':'Updated successfully.', 'status': status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {'message': 'Request Failed', 'status': status.HTTP_400_BAD_REQUEST}

def sendOTP(req):
    try:
        OTP = random.randint(1000, 9999)
        fd = OtpMapping({'email': req['email'], 'otp': OTP})
        emailVerification(req['email'], OTP)
        fd.save()
        return {'message': 'OTP sent successfully.', 'status': status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {'message': 'Request Failed', 'status': status.HTTP_400_BAD_REQUEST}

def verifyEmail(req):
    try:
        res = Otp.objects.filter(email=req['email'], otp=req['otp']).exists()
        if res:
            Otp.objects.filter(email=req['email']).delete()
            return {'message': 'OTP Verified Successfully.', 'status': status.HTTP_200_OK}
        else:
            return {'message': 'OTP Verification Failed.', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print("error", e)
        return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def login(req):
    try:
        if Farmer_registration.objects.filter(farmer_email=req['username'], farmer_password=req['password']).count() > 0:
            res = FarmerSerializer(Farmer_registration.objects.filter(farmer_email=req['username'], farmer_password=req['password']), many=True)
            if res:
                return {'data':res.data, 'status': status.HTTP_200_OK}
            pass
        else:
            return {'message': 'Wrong username or password..', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print("error", e)
        return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def addProduct(req):
    try:
        form = Add_product_mapping(req)
        if form.is_valid():
            form.save()
        return {'message': 'Product added successfully.', 'status': status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {'message': 'Product not added..', 'status': status.HTTP_400_BAD_REQUEST}

def getAllProduct(req):
    try:
        if req['userType'] == 'Admin':
            product_list = ProductSerializers(Products.objects.all(), many=True)
        elif req['userType'] == 'Seller':
            id  =int(req['userId'])
            product_list = ProductSerializers(Products.objects.filter(product_added_by = req['userType']), many=True)
        else:
            product_list = ProductSerializers(Products.objects.all(), many=True)
        return {'data': product_list.data, 'status': status.HTTP_200_OK}
    except Exception as e:
        print('Exception')
        print(e)
        return {'message': 'Something went wrong..', 'status': status.HTTP_400_BAD_REQUEST}

def getProduct(req):
    try:
        if(req['cart'] == True):
            res = Cart.objects.filter(farmer_id=req['farmer_id'])
            if res.count() > 0:
                res = CartSerializerSerializer(res, many=True)
                list = []
                for value in res.data:
                    list.append(value['product_id'])
            product_list = ProductSerializers(Products.objects.filter(product_Id__in =  list), many=True)
        elif(req['wishlist'] == True):
            res = WishList.objects.filter(farmer_id=req['farmer_id'])
            print(res)
            if res.count() > 0:
                res = WishListSerializer(res, many=True)
                list = []
                for value in res.data:
                    list.append(value['product_id'])
            product_list = ProductSerializers(Products.objects.filter(product_Id__in =  list), many=True)
        else:
            product_list = ProductSerializers(Products.objects.filter(product_Id =  req['product_Id']), many=True)
        
        if(len(product_list.data)) > 0 :
            return {'data': product_list.data, 'status': status.HTTP_200_OK}
        else:
            return {'message': 'Something went wrong..', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print(e)
        return {'message': 'Something went wrong..', 'status': status.HTTP_400_BAD_REQUEST}

def updateProduct(req):
    try:
        obj = get_object_or_404(Products, product_Id=req['product_Id'])
        Products.objects.filter( product_Id =  req['product_Id']).update(product_name = req['product_name']
        ,product_category = req['product_category']
        ,product_price = req['product_price']
        ,product_offer = req['product_offer']
        ,product_brand = req['product_brand']
        ,product_description = req['product_description']
        ,product_img = req['product_img']
        ,stock_size = req['stock_size'])
        return {'message': 'Product updated successfully.', 'status': status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {'message': 'Something went wrong', 'status': status.HTTP_400_BAD_REQUEST}

def deleteProduct(req):
    try:
        print(req['product_id'])
        res = Products.objects.filter(product_Id__in = req['product_id'])
        if res.count() > 0:
            res.delete()
            return {'message': 'Product delete successfully.', 'status': status.HTTP_200_OK}
        return {'message': 'Product not found.', 'status': status.HTTP_404_NOT_FOUND}
    except Exception as e:
        print(e)
        return {'message': 'Something went wrong.', 'status': status.HTTP_400_BAD_REQUEST}

def addToCart(req):
    try:
        fd = CartMapping(req)
        if fd.is_valid():
            fd.save()
            return {'message': 'Product Added To Cart.', 'status': status.HTTP_200_OK}
        else:
            return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print(e)
        return {'message': 'Registration Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def getCart(req):
    try:
        res = Cart.objects.filter(farmer_id=req['farmer_id'])
        if res.count() > 0:
            res = CartSerializerSerializer(res, many=True)
            list = []
            for value in res.data:
                list.append(value['product_id'])
            return {'data': list, 'status': status.HTTP_200_OK}
        else:
            return {'message': 'No Product added to cart', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print(e)
        return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def addToWishList(req):
    try:
        fd = WishlistMapping(req)
        print(fd)
        print(fd.is_valid())
        if fd.is_valid():
            fd.save()
            return {'message': 'Product Added To Wishlist.', 'status': status.HTTP_200_OK}
        else:
            return {'message': 'Request Failed.', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}
    except Exception as e:
        print(e)
        return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def getWishList(req):
    try:
        res = WishList.objects.filter(farmer_id=req['farmer_id'])
        if res.count() > 0:
            res = WishListSerializer(res, many=True)
            return {'data': res.data, 'status': status.HTTP_200_OK}
        else:
            return {'message': 'No products in wishlist', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print(e)
        return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def deleteFromWishList(req):
    try:
        WishList.objects.filter(farmer_id=req['farmer_id'], product_id=req['product_id']).delete()
        return {'message': 'Deleted Successfully', 'status': status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def deleteFromCart(req):
    try:
        Cart.objects.filter(farmer_id=req['farmer_id'], product_id=req['product_id']).delete()
        return {'message': 'Deleted Successfully', 'status': status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {'message': e, 'status': status.HTTP_400_BAD_REQUEST}

def getProfileForChat(req):
    try:
        res = Farmer_registration.objects.filter(account_type__in = req['get'])
        print(res)
        res = FarmerSerializer(res, many=True)
        return {'data': res.data, 'status': status.HTTP_200_OK}

    except Exception as e:
        return {'message': e, 'status': status.HTTP_400_BAD_REQUEST}

def sendChat(req):
    try:
        fd = ChatMapping(req)
        print(fd.is_valid())
        print(fd)
        if fd.is_valid():
            fd.save()
            return {'message': 'Message Sent.', 'status': status.HTTP_200_OK}
        else:
            return {'message': 'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print(e)
        return {'message': e, 'status': status.HTTP_400_BAD_REQUEST}

def getChat(req):
    try:
        res = Chat.objects.filter(sender_id__in = [req['receiver_id'], req['sender_id'] ], receiver_id__in = [req['receiver_id'], req['sender_id'] ])
        res = ChatSerializer(res, many=True)
        return {'data': res.data, 'status': status.HTTP_200_OK}

    except Exception as e:
        print(e)
        return {'message': e, 'status': status.HTTP_400_BAD_REQUEST} 

def purches(req):
    try:
        for product in req:
            fd = PurchesMapping(product)
            if fd.is_valid():
                fd.save()
        Cart.objects.filter(farmer_id=req[0]['farmer_id']).delete()
        return {'message': 'Purchess Succsessfull.', 'status': status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {'message': e, 'status': status.HTTP_400_BAD_REQUEST}

def getPurches(req):
    try:
        res = Purches.objects.all()
        res = PurchesSerializer(res, many=True)
        return {'data': res.data, 'status': status.HTTP_200_OK}

    except Exception as e:
        print(e)
        return {'message': e, 'status': status.HTTP_400_BAD_REQUEST} 