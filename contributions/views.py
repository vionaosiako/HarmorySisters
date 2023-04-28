from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
from rest_framework import viewsets
from . import models
from authentication.models import User

# Create your views here.

# @api_view(['GET'])
# def getMonthlyContribution(request):
#     users=MonthlyContribution.objects.all()    
#     serializedData=MonthlyContributionSerializer(instance=users, many=True)
    
#     for value in serializedData.data:
#         user=User.objects.filter(id=value['reg_number']).first()
#         # print(user)
#         value['first_name']=user.first_name
#         value['last_name']=user.last_name

#     return Response(serializedData.data)

@api_view (['GET','POST'])
def getMonthlyContribution(request):

    if request.method == 'GET':
        users=MonthlyContribution.objects.all()    
        serializedData=MonthlyContributionSerializer(instance=users, many=True)
        
        for value in serializedData.data:
            user=User.objects.filter(id=value['reg_number']).first()
            # print(user)
            value['first_name']=user.first_name
            value['last_name']=user.last_name
        return Response(serializedData.data)

    if request.method == 'POST':
        serializedData = MonthlyContributionSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getMonthlyContributionDetails(request,id):
    speficUser = MonthlyContribution.objects.get(pk=id)
    
    if request.method == 'GET':    
        serializedData=MonthlyContributionSerializer(speficUser)
        return Response(serializedData.data)
    
    if request.method == 'PUT':
        serializedData = MonthlyContributionSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
        
        
####
@api_view (['GET','POST'])
def getMerryGoRoundContribution(request):

    if request.method == 'GET':
        users=MerryGoRoundContribution.objects.all()    
        serializedData=MerryGoRoundContributionSerializer(instance=users, many=True)
        
        for value in serializedData.data:
            user=User.objects.filter(id=value['reg_number']).first()
            # print(user)
            value['first_name']=user.first_name
            value['last_name']=user.last_name
        return Response(serializedData.data)

    if request.method == 'POST':
        serializedData = MerryGoRoundContributionSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getMerryGoRoundContributionDetails(request,id):
    speficUser = MerryGoRoundContribution.objects.get(pk=id)
    
    if request.method == 'GET':    
        serializedData=MerryGoRoundContributionSerializer(speficUser)
        return Response(serializedData.data)
    
    if request.method == 'PUT':
        serializedData = MerryGoRoundContributionSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)