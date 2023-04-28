from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

#Create your models here.
class MonthlyContribution(models.Model):
    id = models.AutoField(primary_key=True)
    reg_number =  models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(default=0)
    date_contributed = models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.reg_number)

class MerryGoRoundContribution(models.Model):
    id = models.AutoField(primary_key=True)
    reg_number =  models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(default=0)
    date_contributed = models.DateField(auto_now_add=True,null=True,blank=True)

    
    def __str__(self):
        return str(self.reg_number)