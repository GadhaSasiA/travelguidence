# Generated by Django 5.0.1 on 2024-04-05 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0038_remove_userprofile_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_app.user_reg'),
        ),
    ]
