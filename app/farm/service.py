import json
from farm.models import *
from farm.forms import *
from farm.serializer import *
from rest_framework import status
from .emailService import *
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
import random

def farmer_registration(req):
    try:
        fd = Farmer_registration_mapping(req)
        print(fd)
        print(fd.is_valid())
        if fd.is_valid():
            print("valid")
            is_exists = Farmer_registration.objects.filter(farmer_email=req['farmer_email']).exists()
            print(is_exists)
            if not is_exists:
                fd.save()
                return { 'message' :'Registration Successful.', 'status': status.HTTP_200_OK}
            else:
                return { 'message' :'Registration Failed, User Already Registered.', 'status': status.HTTP_409_CONFLICT}
        else:
            print(fd.errors())
    except Exception as e:
        print(e)
        return { 'message' :'Registration Failed.', 'status': status.HTTP_400_BAD_REQUEST}


def sendOTP(req):
    try:
        OTP= random.randint(1000, 9999)
        fd = OtpMapping({'email':req['email'], 'otp':OTP})
        emailVerification(req['email'], OTP)
        fd.save()
        return { 'message': 'OTP sent successfully.', 'status': status.HTTP_200_OK}
    except Exception as e:
        return { 'message' :'Request Failed', 'status': status.HTTP_400_BAD_REQUEST}


def verifyEmail(req):
    try:
        res = Otp.objects.filter(email=req['email'], otp=req['otp']).exists()
        if res:
            Otp.objects.filter(email=req['email']).delete()
            return { 'message' :'OTP Verified Successfully.', 'status': status.HTTP_200_OK}
        else:
            return { 'message' :'OTP Verification Failed.', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print("error", e)
        return { 'message' :'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}

def login(req):
    try:
        res = Farmer_registration.objects.filter(farmer_email=req['username'],farmer_password=req['password']).count()
        if res:
            return { 'message' :'Login Successful.', 'status': status.HTTP_200_OK}
        else:
            return { 'message' :'Login Failed.', 'status': status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print("error", e)
        return { 'message' :'Request Failed.', 'status': status.HTTP_400_BAD_REQUEST}
