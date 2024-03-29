# Generated by Django 5.0 on 2024-02-16 10:39

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.CharField(max_length=25, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z\\d]{1,24}$', ['First letter uppercase min 2 max 25 characters'])])),
            ],
            options={
                'db_table': 'car_brand',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='CarsModelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cars_model', models.CharField(max_length=25)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_model', to='brand_models.carbrandmodel')),
            ],
            options={
                'db_table': 'cars_model',
                'ordering': ('id',),
            },
        ),
    ]
