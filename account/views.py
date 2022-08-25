from django.shortcuts import render
from django.contrib.auth import login
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer, UserProfileSerializer
from rest_framework import generics



class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data,
            context={'request': self.request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)



class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
