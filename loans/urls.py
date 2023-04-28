from django.urls import path
from .views import *

urlpatterns = [
    path('loancategory/',getLoanCategory,name='loancategory'),
    path('loancategory/<int:id>', getLoanCategoryDetails,name='loancategoryDetails'),
    path('loanrequest/',getLoanRequest,name='loanrequest'),
    path('loanrequest/<int:id>', getLoanRequestDetails,name='loanrequestDetails'),
    path('loanpayment/',getLoanPayment,name='loanpayment'),
    path('loanpayment/<int:id>', getLoanPaymentDetails,name='loanpaymentDetails'),
    
    path('getdashboard/', getDashboard),
    # path('getloanapproved/<int:id>', approved_request)
]