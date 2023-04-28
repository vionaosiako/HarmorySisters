from rest_framework import serializers
from . import models
from .models import NextOfKin,Member

# from RESTJointables.models import MemberJointtable

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'

# class MembersJointableserializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.MemberJointtable
#         fields = '__all__'