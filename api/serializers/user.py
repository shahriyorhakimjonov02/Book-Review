from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=250 ,write_only=True)
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "password")