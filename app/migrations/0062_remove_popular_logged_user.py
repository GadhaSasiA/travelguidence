# Generated by Django 5.0.1 on 2024-04-01 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0061_popular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popular',
            name='logged_user',
        ),
    ]