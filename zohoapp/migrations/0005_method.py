# Generated by Django 4.2.1 on 2023-07-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0004_payment_made_item_delete_payment_made_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(max_length=255)),
            ],
        ),
    ]