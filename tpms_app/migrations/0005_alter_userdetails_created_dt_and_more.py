# Generated by Django 5.0.2 on 2024-02-09 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpms_app', '0004_alter_vehiclemaster_created_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 9, 12, 12, 47, 560942), null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 9, 12, 12, 47, 561941), null=True),
        ),
    ]