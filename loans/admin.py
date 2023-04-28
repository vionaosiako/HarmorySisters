from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LoanRequest),
admin.site.register(LoanPayment),
admin.site.register(LoanCategory),
admin.site.register(CustomerLoan),
