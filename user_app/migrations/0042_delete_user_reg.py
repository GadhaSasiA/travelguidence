# Generated by Django 5.0.1 on 2024-04-06 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide_app', '0036_remove_reply_recipient_remove_reply_sender_and_more'),
        ('user_app', '0041_remove_user_reg_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_reg',
        ),
    ]
