# Generated by Django 3.0.7 on 2020-08-29 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 29, 11, 34, 56, 727881)),
        ),
    ]
