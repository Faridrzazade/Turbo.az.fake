# Generated by Django 5.0.6 on 2024-07-31 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_car_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_approved',
            field=models.BooleanField(default=False, verbose_name='Təsdiq'),
        ),
    ]
