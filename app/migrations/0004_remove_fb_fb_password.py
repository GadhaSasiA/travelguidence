# Generated by Django 5.0.1 on 2024-02-03 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_fb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fb',
            name='fb_password',
        ),
    ]
