# Generated by Django 4.2.1 on 2023-07-24 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0002_alter_payment_made_items_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_made_items',
            name='cash',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.banking'),
        ),
    ]
