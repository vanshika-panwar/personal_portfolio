# Generated by Django 3.0.7 on 2020-09-11 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 11, 12, 48, 51, 882630)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='disription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]