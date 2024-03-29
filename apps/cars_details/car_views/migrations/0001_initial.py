# Generated by Django 5.0 on 2024-02-16 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarViewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('car_ad', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='car_views', to='cars.carmodel')),
            ],
            options={
                'db_table': 'car_views',
            },
        ),
    ]
