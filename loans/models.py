from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
# Create your models here.
STATUS =(
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
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

    def save_instance(self):
        self.save()

    
class CustomerLoan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_user')
    total_loan = models.PositiveIntegerField(default=0)
    payable_loan = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=LoanRequest, dispatch_uid='create_customer_loan')
def create_customer_loan(sender, instance, created, **kwargs):
    print(kwargs)
    # if created or kwargs.get('update_fields') == {'status'}:
    if instance.status == 'Approved':
        interest = instance.amount_requested * 0.1  # calculate interest (10% of amount_requested)
        customer_loan = CustomerLoan.objects.create(
            user=instance.user,
            total_loan=instance.amount_requested
        )
        customer_loan.payable_loan = instance.amount_requested + interest
        customer_loan.save()

@receiver(pre_delete, sender=LoanRequest, dispatch_uid='delete_customer_loan')
def delete_customer_loan(sender, instance, **kwargs):
    try:
        customer_loan = CustomerLoan.objects.get(user=instance.user)
        customer_loan.delete()
    except CustomerLoan.DoesNotExist:
        pass

class LoanPayment(models.Model):
    payment_id = models.CharField(max_length=6, primary_key=True, editable=False, unique=True)
    loan_id = models.ForeignKey(LoanRequest, on_delete=models.CASCADE)
    amount_paid = models.IntegerField(default=0)
    date_paid = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.loan_id)

    def save(self, *args, **kwargs):
        if not self.payment_id:
            self.payment_id = get_random_string(length=6, allowed_chars='123456')
        super().save(*args, **kwargs)

@receiver(post_save, sender=LoanRequest, dispatch_uid='create_loan_payment')
def create_loan_payment(sender, instance, **kwargs):
    if instance.status == 'Approved':
        # Create a new LoanPayment object
        payment = LoanPayment()
        
        # Set the relevant fields in the LoanPayment object
        payment.loan_id = instance
        # Set other fields as needed
        
        # Save the LoanPayment object
        payment.save()
        