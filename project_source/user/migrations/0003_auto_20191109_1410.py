# Generated by Django 2.2.1 on 2019-11-09 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usertoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='expire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 14, 10, 8, 143088)),
        ),
    ]
