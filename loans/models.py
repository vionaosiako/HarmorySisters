from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.crypto import get_random_string
# Create your models here.
STATUS =(
    ("Approved", "Approved"),
    ("Disapproved", "Disapproved"),
    ("Pending", "Pending"),
    )

class LoanCategory(models.Model):
    loan_name = models.CharField(max_length=250)
    creation_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_name
class LoanRequest(models.Model):
    id =models.CharField(max_length=6, primary_key = True, editable=False, unique=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(LoanCategory, on_delete=models.CASCADE, null=True)
    amount_requested = models.IntegerField(default=0)
    purpose = models.TextField(null=True,blank=True)
    status = models.TextField(choices=STATUS, blank=False, default='Pending')
    payment_period_years = models.PositiveIntegerField(default=1)
    date_requested = models.DateField(auto_now_add=True,null=True,blank=True)
    status_date = models.CharField(max_length=150, null=True, blank=True, default=None)
    
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Loan Request"
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_random_string(length=6, allowed_chars='123456')
        return super(LoanRequest, self).save(*args, **kwargs)
    
class LoanPayment(models.Model):
    payment_id = models.CharField(max_length=6, primary_key = True, editable=False, unique=True)
    loan_id =  models.ForeignKey(LoanRequest, on_delete=models.CASCADE)
    amount_paid = models.IntegerField(default=0)
    date_paid = models.DateField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    def __str__(self):
        return self.loan_id.reg_number.username
    def save(self, *args, **kwargs):
        if not self.payment_id:
            self.payment_id = get_random_string(length=6, allowed_chars='123456')
        return super(LoanPayment, self).save(*args,**kwargs)

class CustomerLoan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_user')
    total_loan = models.PositiveIntegerField(default=0)
    payable_loan = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username