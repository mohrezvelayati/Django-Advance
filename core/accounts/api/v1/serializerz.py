from typing import Any, Dict
from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Profile



class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError({'detail':'password doesnt match'})
        
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})


    
    def create(self, validated_data):
        return super().create(validated_data)



class CustomAuthTokenSerializer(serializers.Serializer):
    # gets email 
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    # checks validation of username & password
    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
            if not user.is_verified:
                raise serializers.ValidationError({'details':'user is not verified'})
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['email'] = self.user.email
        validated_data['user_id'] = self.user.id
        return validated_data
    


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)
    conform_password = serializers.CharField(required = True)
    
    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('conform_password'):
            raise serializers.ValidationError({'detail':'password doesnt match'})
        
        try:
            validate_password(attrs.get('new_password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'new_password':list(e.messages)})

        return super().validate(attrs)
    


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source = 'user.email', read_only = True)

    class Meta:
        model = Profile
        fields = ('user_id', 'email', 'first_name', 'last_name', 'image', 'description')
        read_only_field = ['email']