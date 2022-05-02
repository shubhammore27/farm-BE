from django.urls import re_path as url
from . import views

# app_name = 'client'

urlpatterns = [
    url(r'check', views.check, name='check'),
    url(r'farmer_registration', views.farmer_registration, name='farmer_registration'),
    ]