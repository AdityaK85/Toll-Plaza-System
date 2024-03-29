# Generated by Django 5.0.2 on 2024-03-03 15:16

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpms_app', '0015_auto_20240215_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 3, 20, 46, 29, 679342), null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 3, 20, 46, 29, 680341), null=True),
        ),
        migrations.CreateModel(
            name='PasswordRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(blank=True, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tpms_app.userdetails')),
            ],
        ),
    ]
