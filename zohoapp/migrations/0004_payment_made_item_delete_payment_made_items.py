# Generated by Django 4.2.1 on 2023-07-24 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0003_alter_payment_made_items_cash'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_made_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField(blank=True, max_length=255, null=True)),
                ('payment', models.TextField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('current_balance', models.IntegerField(blank=True, null=True)),
                ('gst', models.TextField(blank=True, max_length=255, null=True)),
                ('cash', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.banking')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_table')),
            ],
        ),
        migrations.DeleteModel(
            name='payment_made_items',
        ),
    ]
