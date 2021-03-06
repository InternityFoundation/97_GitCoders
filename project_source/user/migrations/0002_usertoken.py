# Generated by Django 2.2.1 on 2019-09-21 08:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(blank=True, null=True)),
                ('token_type', models.PositiveIntegerField(choices=[(1, 'New Account'), (2, 'Forget Password')], default=1)),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 22, 13, 30, 9, 598574))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
