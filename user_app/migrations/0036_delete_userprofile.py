# Generated by Django 5.0.1 on 2024-04-04 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0035_delete_direct_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
