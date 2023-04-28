from django.urls import path
from .views import *

urlpatterns = [
    path('message/',send_sms,name='message'),
]