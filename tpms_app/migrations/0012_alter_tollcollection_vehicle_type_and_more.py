# Generated by Django 5.0.2 on 2024-02-13 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpms_app', '0011_alter_tollcollection_vehicle_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tollcollection',
            name='vehicle_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 10, 21, 26, 45418), null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 10, 21, 26, 46417), null=True),
        ),
    ]