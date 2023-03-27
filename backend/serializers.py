from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()
from .models import Hospital,DoctorProfile,Report

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer):
        model=User
        fields=['id','email','name','password','is_verified']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','first_name','last_name','profile_picture']
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields="__all__"

class profileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    hospital=HospitalSerializer()
    class Meta:
        model=DoctorProfile
        fields="__all__"
class reportSerializer(serializers.ModelSerializer):
    patient=UserSerializer()
    class Meta:
        model=Report
        fields="__all__"