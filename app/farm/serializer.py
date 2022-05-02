from rest_framework import serializers
from farm.models import *


class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = ['id', 'otp', 'email']