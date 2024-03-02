# Generated by Django 3.2.24 on 2024-02-15 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpms_app', '0014_auto_20240215_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='salary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 15, 8, 43, 51, 938911), null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 15, 8, 43, 51, 939910), null=True),
        ),
    ]