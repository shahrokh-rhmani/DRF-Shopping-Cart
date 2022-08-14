from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label = "Username",
        write_only =True
    )

    password = serializers.CharField(
        label = "Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
