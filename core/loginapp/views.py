from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .serializers import AuthTokenSerializer, UserLoginSerializer
from utils import common

# Create your views here.


class SignUpView(APIView):
    commonUtils = common.CommonUtilities()

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return self.commonUtils.get_response(
                success=True,
                serializer=serializer,  # Use serializer.data for serialized user data
                status_name=status.HTTP_201_CREATED,
                token=token.key,
            )

        return self.commonUtils.get_response(
            success=False,
            serializer=serializer.errors,  # Use serializer.errors for error messages
            status_name=status.HTTP_400_BAD_REQUEST,
        )


class LoginView(APIView):
    commonUtils = common.CommonUtilities()

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserLoginSerializer(user)
            return self.commonUtils.get_response(
                success=True,
                serializer=user_serializer,
                status_name=status.HTTP_201_CREATED,
                token=token.key,
            )
        return self.commonUtils.get_response(
            serializer=serializer,
            status_name=status.HTTP_400_BAD_REQUEST,
        )
