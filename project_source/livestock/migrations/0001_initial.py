# Generated by Django 2.2.1 on 2019-11-09 08:40

from django.db import migrations, models
import django.db.models.deletion
import livestock.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=livestock.models.upload_livestock_image_directory_path)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=livestock.models.upload_livestock_image_directory_path)),
                ('disease_name', models.CharField(max_length=120, verbose_name='Disease')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryBImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=livestock.models.upload_livestock_image_directory_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.CategoryB', verbose_name='Category B')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryAImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=livestock.models.upload_livestock_image_directory_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.CategoryA', verbose_name='Category A')),
            ],
        ),
    ]
