# Generated by Django 5.1.3 on 2024-11-14 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('Gas Leak', 'Gas Leak'), ('Maintenance', 'Maintenance'), ('Billing', 'Billing'), ('Other', 'Other')], max_length=20)),
                ('details', models.TextField()),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('resolution_date', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_service.customer')),
            ],
        ),
    ]
