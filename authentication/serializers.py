from rest_framework import serializers
from . import models
from .models import Admin, Client, NextOfKin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ['password']


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = models.User
        fields = ['id','username', 'first_name', 'last_name','othername','gender','residential_area','national_id','date_of_birth','phone_number','email', 'password', 'password2','date_joined']

    def save(self, **kwargs):
        user = models.User(
            # reg_number=self.validated_data['reg_number'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            othername=self.validated_data['othername'],
            gender=self.validated_data['gender'],
            phone_number=self.validated_data['phone_number'],
            residential_area=self.validated_data['residential_area'],
            national_id=self.validated_data['national_id'],
            date_of_birth=self.validated_data['date_of_birth'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.is_staff = True
        user.save()
        models.Admin.objects.create(user=user)
        return user


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = models.User
        # fields = ['username','first_name', 'last_name', 'email', 'password', 'password2']
        fields = ['id','username', 'first_name', 'last_name','othername','gender','residential_area','national_id','date_of_birth','phone_number','email', 'password', 'password2','date_joined']

        # extra_kwargs = {
        #     'password':{'write_only':True}
        # }

    def save(self, **kwargs):
        user = models.User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            othername=self.validated_data['othername'],
            gender=self.validated_data['gender'],
            phone_number=self.validated_data['phone_number'],
            residential_area=self.validated_data['residential_area'],
            national_id=self.validated_data['national_id'],
            date_of_birth=self.validated_data['date_of_birth'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.is_client = True
        user.save()
        models.Client.objects.create(user=user)
        return user