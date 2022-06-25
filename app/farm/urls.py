from django.urls import re_path as url
from . import views
from django.conf.urls.static import static  
from django.conf import settings 

# app_name = 'client'

urlpatterns = [
    url(r'check', views.check, name='check'),
    url(r'farmer_registration', views.farmer_registration, name='farmer_registration'),
    url(r'sendOTP', views.sendOTP, name='index'),
    url(r'verifyEmail', views.verifyEmail, name='index'),
    url(r'login', views.login, name='login'),
    url(r'add_product', views.add_product, name='add-product'),
    
    ]


if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  