# Generated by Django 5.0.1 on 2024-03-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0027_alter_user_reg_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='profile_image',
            field=models.ImageField(default='default_profile_image.jpg', upload_to='profile_images'),
        ),
    ]
