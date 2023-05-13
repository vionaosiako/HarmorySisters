from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
from .models import *
from .serializers import *
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
#Loan approved
#-------------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET','PUT','DELETE'])
def approved_request(request, id):
    speficLoanRequest = LoanRequest.objects.get(pk=id)
    
    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    speficLoanRequest.status_date = status_date
    speficLoanRequest.save()
    year = speficLoanRequest.payment_period_years

    approved_user = LoanRequest.objects.get(id=id).user
    if CustomerLoan.objects.filter(user=approved_user).exists():

        # find previous amount of user
        PreviousAmount = CustomerLoan.objects.get(
            user=approved_user).total_loan
        PreviousPayable = CustomerLoan.objects.get(
            user=approved_user).payable_loan

        # update balance
        CustomerLoan.objects.filter(
            user=approved_user).update(total_loan=int(PreviousAmount)+int(loan_obj.amount_requested))
        CustomerLoan.objects.filter(
            user=approved_user).update(payable_loan=int(PreviousPayable)+int(loan_obj.amount_requested)+int(loan_obj.amount_requested)*0.12*int(year))

    else:

        # request user

        # CustomerLoan object create
        save_loan = CustomerLoan()

        save_loan.customer = approved_user
        save_loan.total_loan = int(speficLoanRequest.amount_requested)
        save_loan.payable_loan = int(
            speficLoanRequest.amount_requested)+int(speficLoanRequest.amount_requested)*0.12*int(year)
        save_loan.save()

    loanRequest.objects.filter(id=id).update(status='approved')
    loanrequest = loanRequest.objects.filter(status='pending')
    # return render(request, 'admin/request_user.html', context={'loanrequest': loanrequest})
    return JsonResponse(context={'loanrequest': loanrequest})
#-------------------------------------------------------------------------------------------------------------------------------------
#Loan disapproved
#-------------------------------------------------------------------------------------------------------------------------------------

def rejected_request(request, id):

    today = date.today()
    status_date = today.strftime("%B %d, %Y")
    loan_obj = loanRequest.objects.get(id=id)
    loan_obj.status_date = status_date
    loan_obj.save()
    # rejected_customer = loanRequest.objects.get(id=id).customer
    # print(rejected_customer)
    loanRequest.objects.filter(id=id).update(status='rejected')
    loanrequest = loanRequest.objects.filter(status='pending')
    return render(request, 'admin/request_user.html', context={'loanrequest': loanrequest})

#-------------------------------------------------------------------------------------------------------------------------------------
#Loan processes
#-------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
def getDashboard(request):
    if request.method == 'GET':
        totalCustomer = User.objects.all().count()
        requestLoan = LoanRequest.objects.all().filter(status='Pending').count()
        approved = LoanRequest.objects.all().filter(status='Approved').count()
        rejected = LoanRequest.objects.all().filter(status='Rejected').count()
        totalLoan = CustomerLoan.objects.aggregate(Sum('total_loan'))['total_loan__sum']
        totalPayable = CustomerLoan.objects.aggregate(Sum('payable_loan'))['payable_loan__sum']
        totalPaid = LoanPayment.objects.aggregate(Sum('amount_paid'))['amount_paid__sum']

        # Extract values from tuples or assign default value of 0
        totalLoan = totalLoan or 0
        totalPayable = totalPayable or 0
        totalPaid = totalPaid or 0

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
        }
        print(dict)

    # return render(request, 'admin/dashboard.html', context=dict)
    return JsonResponse(dict)
