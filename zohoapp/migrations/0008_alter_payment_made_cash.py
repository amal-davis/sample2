# Generated by Django 4.2.1 on 2023-08-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0007_payment_made_delete_payment_made_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_made',
            name='cash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
