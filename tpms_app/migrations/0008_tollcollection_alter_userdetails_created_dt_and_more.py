# Generated by Django 5.0.2 on 2024-02-10 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpms_app', '0007_remove_tollinfo_valid_dt_tollinfo_valid_toll_hr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TollCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_identification', models.CharField(blank=True, max_length=200, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=200, null=True)),
                ('toll_calculation', models.CharField(blank=True, max_length=200, null=True)),
                ('fee_sehedule', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_by', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_recipt', models.FileField(blank=True, null=True, upload_to='payment_recipt')),
                ('lane', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 10, 9, 2, 50, 894008), null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 10, 9, 2, 50, 895007), null=True),
        ),
    ]