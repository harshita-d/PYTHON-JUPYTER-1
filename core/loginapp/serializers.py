from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from loginapp import models
from django.utils.translation import gettext_lazy as _


class UserLoginSerializer(serializers.ModelSerializer):
    """serializer for user profile"""

    class Meta:
        model = models.UserLoginProfile
        fields = ("email", "username")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return models.UserLoginProfile.objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                username=email,
                password=password,
            )
            if not user:
                raise serializers.ValidationError(
                    {"detail": _("Unable to login with the provided credentials.")},
                    code="authorization",
                )
        else:
            raise serializers.ValidationError(
                {"detail": _("Must include email and password.")}, code="authorization"
            )

        attrs["user"] = user
        return attrs
