    
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import africastalking
import requests
from django.conf import settings
import os

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
    recipients = ["+254703616854"]#"+254768852080"

    # Set your message
    message = "Hello. Regards TheLioness"

    # Set your shortCode or senderId
    # sender = "shortCode or senderId"
    try:
        # Thats it, hit send and we'll take care of the rest.
        response = sms.send(message, recipients)
        print("am response sms", response)
        return HttpResponse(response)
    except Exception as e:
        return HttpResponse('Encountered an error while sending: %s' % str(e))

