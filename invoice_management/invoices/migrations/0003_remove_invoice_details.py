# Generated by Django 5.0 on 2023-12-31 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_invoice_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='details',
        ),
    ]
