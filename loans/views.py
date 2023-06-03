from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
from .models import *
from .serializers import *
from contributions.models import MonthlyContribution
from authentication.models import User
from django.http import JsonResponse
from datetime import date
from django.db.models import Sum


# Create your views here.

#-------------------------------------------------------------------------------------------------------------------------------------
#Loan Category
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view (['GET','POST'])
def getLoanCategory(request):

    if request.method == 'GET':
        users=LoanCategory.objects.all()    
        serializedData=LoanCategorySerializer(instance=users, many=True)
        return Response(serializedData.data)

    if request.method == 'POST':
        serializedData = LoanCategorySerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getLoanCategoryDetails(request,id):
    speficLoanCategory = LoanCategory.objects.get(pk=id)
    
    if request.method == 'GET':    
        serializedData=LoanCategorySerializer(speficLoanCategory)
        return Response(serializedData.data)
    
    if request.method == 'PUT':
        serializedData = LoanCategorySerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
    
    if request.method == 'DELETE':
        speficLoanCategory = LoanCategory.objects.get(pk=id)
        speficLoanCategory.delete()
        return Response('Loan Category Successfully Deleted!')
    
    
#-------------------------------------------------------------------------------------------------------------------------------------
#Loan Request
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view (['GET','POST'])
def getLoanRequest(request):

    if request.method == 'GET':
        users=LoanRequest.objects.all()        
        serializedData=LoanRequestSerializer(instance=users, many=True)
        return Response(serializedData.data)

    if request.method == 'POST':
        serializedData = LoanRequestSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getLoanRequestDetails(request,id):
    speficLoanRequest = LoanRequest.objects.get(pk=id)
    
    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    # loan_obj = LoanRequest.objects.get(pk=id)
    speficLoanRequest.status_date = status_date
    speficLoanRequest.save()
    year = speficLoanRequest.payment_period_years
    
    if request.method == 'GET':   
        serializedData=LoanRequestSerializer(speficLoanRequest)
        return Response(serializedData.data)
    
    if request.method == 'PUT':
        serializedData = LoanRequestSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
    
    if request.method == 'DELETE':
        speficLoanRequest = LoanRequest.objects.get(pk=id)
        speficLoanRequest.delete()
        return Response('Loan Request Successfully Deleted!')

#-------------------------------------------------------------------------------------------------------------------------------------
#Loan Payment
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view (['GET','POST'])
def getLoanPayment(request):

    if request.method == 'GET':
        users=LoanPayment.objects.all()    
        serializedData=LoanPaymentSerializer(instance=users, many=True)
        return Response(serializedData.data)

    if request.method == 'POST':
        serializedData = LoanPaymentSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)

@api_view(['GET','PUT','DELETE'])
def getLoanPaymentDetails(request,id):
    speficLoanPayment = LoanPayment.objects.get(pk=id)
    
    if request.method == 'GET':    
        serializedData=LoanPaymentSerializer(speficLoanPayment)
        return Response(serializedData.data)
    
    if request.method == 'PUT':
        serializedData = LoanPaymentSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
    
    if request.method == 'DELETE':
        speficLoanPayment = LoanPayment.objects.get(pk=id)
        speficLoanPayment.delete()
        return Response('Loan Payment Successfully Deleted!')

#-------------------------------------------------------------------------------------------------------------------------------------
#Pending Loans
#-------------------------------------------------------------------------------------------------------------------------------------
@api_view (['GET'])
def getPendingLoans(request):
    if request.method == 'GET':
        loanApproved = LoanRequest.objects.filter(status='Pending')
        serializedData = LoanRequestSerializer(instance = loanApproved, many=True)
        for value in serializedData.data:
            user=User.objects.filter(id=value['user']).first()
            value['first_name']=user.first_name
            value['last_name']=user.last_name
        return Response(serializedData.data)

#-------------------------------------------------------------------------------------------------------------------------------------
#Loan approved
#-------------------------------------------------------------------------------------------------------------------------------------
@api_view (['GET'])
def getApprovedLoans(request):
    if request.method == 'GET':
        loanApproved = LoanRequest.objects.filter(status='Approved')
        serializedData = LoanRequestSerializer(instance = loanApproved, many=True)
        for value in serializedData.data:
            user=User.objects.filter(id=value['user']).first()
            value['first_name']=user.first_name
            value['last_name']=user.last_name
        return Response(serializedData.data)
#-------------------------------------------------------------------------------------------------------------------------------------
#Loan disapproved
#-------------------------------------------------------------------------------------------------------------------------------------
@api_view (['GET'])
def getRejectedLoans(request):
    if request.method == 'GET':
        loanRejected = LoanRequest.objects.filter(status='Rejected')
        serializedData = LoanRequestSerializer(instance = loanRejected, many=True)
        for value in serializedData.data:
            user=User.objects.filter(id=value['user']).first()
            value['first_name']=user.first_name
            value['last_name']=user.last_name
        return Response(serializedData.data)

#-------------------------------------------------------------------------------------------------------------------------------------
#Loan processes
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
def getDashboard(request):
    if request.method == 'GET':
        totalCustomer = User.objects.all().count()
        requestLoan = LoanRequest.objects.all().filter(status='Pending').count()
        totalContribution = MonthlyContribution.objects.aggregate(Sum('Amount'))['Amount__sum']
        approved = LoanRequest.objects.all().filter(status='Approved').count()
        rejected = LoanRequest.objects.all().filter(status='Rejected').count()
        totalLoan = CustomerLoan.objects.aggregate(Sum('total_loan'))['total_loan__sum']
        totalPayable = CustomerLoan.objects.aggregate(Sum('payable_loan'))['payable_loan__sum']
        totalPaid = LoanPayment.objects.aggregate(Sum('amount_paid'))['amount_paid__sum']

        # Extract values from tuples or assign default value of 0
        totalLoan = totalLoan or 0
        totalPayable = totalPayable or 0
        totalPaid = totalPaid or 0
        totalContribution = totalContribution or 0

        totalOutstandingLoan = int(totalPayable) - int(totalPaid)

        dict = {
            'Total Members': totalCustomer,
            'Request Loan': requestLoan,
            'Approved Loan': approved,
            'Rejected Loan': rejected,
            'Total Loan': totalLoan,
            'Total Payable': totalPayable,
            'Total Paid': totalPaid,
            'Total Outstanding Loan': totalOutstandingLoan,
            'Total Contribution': totalContribution
        }
        print(dict)

    # return render(request, 'admin/dashboard.html', context=dict)
    return JsonResponse(dict)

