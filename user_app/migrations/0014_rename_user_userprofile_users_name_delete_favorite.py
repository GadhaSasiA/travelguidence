# Generated by Django 5.0.1 on 2024-03-11 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0013_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='users_name',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]