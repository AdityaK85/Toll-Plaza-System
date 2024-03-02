# Generated by Django 5.0.2 on 2024-02-13 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpms_app', '0008_tollcollection_alter_userdetails_created_dt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tollcollection',
            name='addr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tollcollection',
            name='lane_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tollcollection',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tollcollection',
            name='veh_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 9, 7, 27, 413293), null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 9, 7, 27, 414294), null=True),
        ),
    ]
