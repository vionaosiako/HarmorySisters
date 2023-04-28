from rest_framework import serializers
from . import models
from .models import MonthlyContribution,MerryGoRoundContribution

class MonthlyContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MonthlyContribution
        fields = '__all__'
        
class MerryGoRoundContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MerryGoRoundContribution
        fields = '__all__'
        

def monthlycontribution (self, **kwargs):
    monthlycontribution = models.MonthlyContribution(
        reg_number=self.validated_data['reg_number'],
        Amount=self.validated_data['Amount'],
    )

    monthlycontribution.save()
    models.MonthlyContribution.objects.create()
    return monthlycontribution