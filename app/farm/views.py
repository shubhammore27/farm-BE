from django.shortcuts import render
from . import service
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


# EXAMPLE

# @api_view(['POST'])
# def savePrediction(req):
#     try:
#         print("Saving prediction")
#         res = service.savePrediction(req.data)
#         return Response(res, status = status.HTTP_200_OK)
#     except Exception as e:
#         print(e)
#         return Response(status = status.HTTP_400_BAD_REQUEST)
