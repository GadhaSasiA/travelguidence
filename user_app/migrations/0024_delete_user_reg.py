# Generated by Django 5.0.1 on 2024-03-30 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0023_user_reg_delete_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_reg',
        ),
    ]
