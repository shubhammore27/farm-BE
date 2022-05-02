from django.forms import ModelForm
from farm.models import *


class Farmer_registration_mapping(ModelForm):
    class Meta:
        model = Farmer_registration
        fields = "__all__"


class OtpMapping(ModelForm):
    class Meta:
        model = Otp
        fields = "__all__"