# Generated by Django 5.0.4 on 2024-07-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_car_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecar',
            name='image',
            field=models.ImageField(default=1, upload_to='user/img_cars', verbose_name='Şəkil'),
            preserve_default=False,
        ),
    ]