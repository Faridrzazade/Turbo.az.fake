# Generated by Django 5.0.6 on 2024-08-05 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
