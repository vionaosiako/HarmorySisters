# Generated by Django 4.1 on 2023-04-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanpayment',
            old_name='payment_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='status',
            field=models.TextField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending'),
        ),
    ]
