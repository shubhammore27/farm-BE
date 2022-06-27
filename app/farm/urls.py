from django.urls import re_path as url
from . import views
from django.conf.urls.static import static  
from django.conf import settings 

# app_name = 'client'

urlpatterns = [
    url(r'check', views.check, name='check'),
    url(r'farmer_registration', views.farmer_registration, name='farmer_registration'),
    url(r'getFarmerDetails', views.getFarmerDetails, name='getFarmerDetails'),
    url(r'updateProfile', views.updateProfile, name='updateProfile'),
    

    url(r'sendOTP', views.sendOTP, name='index'),
    url(r'verifyEmail', views.verifyEmail, name='index'),
    url(r'login', views.login, name='login'),


    # ADMIN API'S
    url(r'add_product', views.add_product, name='add-product'),
    url(r'get_all_product', views.get_all_product, name='get-all-product'),
    url(r'get_product', views.get_product, name='get-product'),
    url(r'update_product', views.update_product, name='update-product'),
    url(r'deleteProduct', views.deleteProduct, name='delete-product'),
    
    ]


if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  