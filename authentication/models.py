from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import date
from random import randint
# from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    othername = models.CharField(max_length=100)
    gender = models.CharField(max_length=15)
    residential_area = models.CharField(max_length=100)
    national_id = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_joined']
    
    def __str__(self):
        return str(self.username)
    
    def calculate_age(date_of_birth):
        today = date.today()
        return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Admin(models.Model):
    user = models.OneToOneField(User, related_name='admins', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return str(self.user.username)

class NextOfKin(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    national_id = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    percentage = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nextofkin')
    
    def __str__(self):
        return self.surname
