# Generated by Django 5.0 on 2023-12-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='details',
            field=models.JSONField(default=list),
        ),
    ]
