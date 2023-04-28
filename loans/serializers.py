from rest_framework import serializers
from . import models
from .models import *

class LoanCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanCategory
        fields = '__all__'

class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'

class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = '__all__'