# Generated by Django 5.0.2 on 2024-02-13 18:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpms_app', '0010_remove_tollcollection_lane_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tollcollection',
            name='vehicle_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tpms_app.tollinfo'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 10, 19, 50, 530278), null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 10, 19, 50, 530278), null=True),
        ),
    ]