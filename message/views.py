from django.shortcuts import render
from django.http import HttpResponse
import africastalking
import requests
from django.conf import settings
import os
from .models import *
from .serializers import *
from authentication.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

@api_view (['POST'])
@csrf_exempt
def send_sms(request):
    # Set your app credentials
    username = os.environ.get('USER1')
    api_key = os.environ.get('API_KEY')
    
    url = 'https://api.africastalking.com/version1/messaging'
    headers = {'Authorization': 'Bearer %s' % os.getenv('API_KEY')}
    response = requests.get(url, headers=headers)   

    # Initialize the SDK
    africastalking.initialize(username, api_key)

    # Get the SMS service
    sms = africastalking.SMS

    # Set the numbers you want to send to in international format
    phoneList=[]
    recipients = User.objects.all()
    # for recipient in recipients:
    
    # #"+254768852080"

    # # Set your message
    #     message = request.data['message']
       
    #     try:
    #         # Thats it, hit send and we'll take care of the rest.
    #         response = sms.send(message, ["+254{}".format(recipient.phone_number[1:])])
    #         # response = sms.send(message, ["+254{}".format(recipient.phone_number[1:100])])
    #         print("am response sms", response)
    #         return HttpResponse(response)
    #     except Exception as e:
    #         return HttpResponse('Encountered an error while sending: %s' % str(e))

    for recipient in recipients:
        message = request.data['message']
        phone_number = "+254{}".format(recipient.phone_number[1:])
        try:
            response = sms.send(message, [phone_number])
            print("SMS response:", response)
        except Exception as e:
            print("Error sending SMS:", str(e))        

