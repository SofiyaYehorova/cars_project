# Generated by Django 5.0 on 2024-02-16 10:39

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand_models', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100000000)], verbose_name=django.core.validators.MinValueValidator(0))),
                ('currency', models.CharField(choices=[('USD', 'Usd'), ('EUR', 'Eur'), ('UAH', 'Uah')], default='UAH', max_length=3)),
                ('region', models.CharField(max_length=25)),
                ('brand', models.ForeignKey(error_messages='If your brand_models is missing, contact the administrator', on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='brand_models.carbrandmodel')),
                ('cars_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='brand_models.carsmodelmodel')),
                ('premium_seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='premium_seller', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cars',
                'ordering': ('id',),
            },
        ),
    ]
