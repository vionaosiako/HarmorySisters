# Generated by Django 4.1 on 2023-04-26 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_name', models.CharField(max_length=250)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoanRequest',
            fields=[
                ('id', models.CharField(editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('amount_requested', models.IntegerField(default=0)),
                ('purpose', models.TextField(blank=True, null=True)),
                ('status', models.TextField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Pending', 'Pending')], default='Pending')),
                ('payment_period_years', models.PositiveIntegerField(default=1)),
                ('date_requested', models.DateField(auto_now_add=True, null=True)),
                ('status_date', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loans.loancategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Loan Request',
            },
        ),
        migrations.CreateModel(
            name='LoanPayment',
            fields=[
                ('payment_id', models.CharField(editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('amount_paid', models.IntegerField(default=0)),
                ('date_paid', models.DateField(auto_now_add=True)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.loanrequest')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_loan', models.PositiveIntegerField(default=0)),
                ('payable_loan', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
