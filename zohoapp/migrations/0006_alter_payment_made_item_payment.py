# Generated by Django 4.2.1 on 2023-07-25 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0005_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_made_item',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.method'),
        ),
    ]
