from django.urls import re_path as url
from . import views
from django.conf.urls.static import static  
from django.conf import settings 

# app_name = 'client'

urlpatterns = [

    # Common API's
    url(r'check', views.check, name='check'),
    url(r'farmer_registration', views.farmer_registration, name='farmer_registration'),
    url(r'getFarmerDetails', views.getFarmerDetails, name='getFarmerDetails'),
    url(r'updateProfile', views.updateProfile, name='updateProfile'),
    url(r'sendOTP', views.sendOTP, name='index'),
    url(r'verifyEmail', views.verifyEmail, name='index'),
    url(r'login', views.login, name='login'),
    # CHAT
    url(r'getChat', views.getChat, name='getChat'),
    url(r'sendChat', views.sendChat, name='sendChat'),
    url(r'auth', views.auth, name='auth'),
    url(r'getProfileForChat', views.getProfileForChat, name='getProfileForChat'),
    url(r'sendChat', views.sendChat, name='sendChat'),
    # Farmers API's
    url(r'getCart', views.getCart, name='getCart'),
    url(r'addToCart', views.addToCart, name='addToCart'),
    url(r'getWishList', views.getWishList, name='getWishList'),
    url(r'addToWishList', views.addToWishList, name='addToWishList'),
    url(r'deleteFromWishList', views.deleteFromWishList, name='deleteFromWishList'),
    url(r'deleteFromCart', views.deleteFromCart, name='deleteFromCart'),
    # ADMIN API's
    url(r'add_product', views.add_product, name='add-product'),
    url(r'get_all_product', views.get_all_product, name='get-all-product'),
    url(r'get_product', views.get_product, name='get-product'),
    url(r'update_product', views.update_product, name='update-product'),
    url(r'deleteProduct', views.deleteProduct, name='delete-product'),
    
    ]


if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  