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
        return Response(res, status = status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)
