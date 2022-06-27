from django.shortcuts import render
from . import service
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def check(req):
    res = {'message':'', 'status':status.HTTP_400_BAD_REQUEST}
    return Response(res)

@api_view(['POST'])
def farmer_registration(req):
    try:
        res = service.farmer_registration(req.data)
        return Response(res, status = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def getFarmerDetails(req):
    try:
        res = service.getFarmerDetails(req.data)
        return Response(res, status = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST) 


@api_view(['POST'])
def updateProfile(req):
    try:
        res = service.updateProfile(req.data)
        return Response(res, status = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sendOTP(req):
    try:
        res = service.sendOTP(req.data)
        return Response(res, status = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verifyEmail(req):
    try:
        res = service.verifyEmail(req.data)
        print(res)
        return Response(res, status = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(req):
    try:
        print(req.data)
        res = service.login(req.data)
        return Response(res)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_product(req):
    try:
        res = service.addProduct(req.data)
        return Response(res)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def get_all_product(req):
    try:
        res = service.getAllProduct(req.data)
        return Response(res)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_product(req):
    try:
        res = service.getProduct(req.data)
        return Response(res)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_product(req):
    try:
        res = service.updateProduct(req.data)
        return Response(res)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def deleteProduct(req):
    try:
        res = service.deleteProduct(req.data)
        return Response(res)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)




