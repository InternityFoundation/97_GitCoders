# Generated by Django 2.2.1 on 2019-11-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0002_categoryb_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStockDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Disease Name')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
                ('causes', models.TextField(blank=True, null=True, verbose_name='Causes')),
                ('mode_of_transmission', models.TextField(blank=True, null=True, verbose_name='Mode Of Transmission')),
                ('symptoms', models.TextField(blank=True, null=True, verbose_name='Symptoms')),
                ('diagnostic_tests', models.TextField(blank=True, null=True, verbose_name='Diagnostic Tests')),
                ('preventive_methods', models.TextField(blank=True, null=True, verbose_name='Preventive Methods')),
                ('suggested_first_aid', models.TextField(blank=True, null=True, verbose_name='Suggested First Aid')),
                ('constrol_measures', models.TextField(blank=True, null=True, verbose_name='Control Measures')),
            ],
        ),
    ]
