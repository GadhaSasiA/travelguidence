# Generated by Django 5.0.1 on 2024-04-06 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide_app', '0039_remove_reply_recipient_remove_reply_sender_and_more'),
        ('user_app', '0047_delete_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_reg',
        ),
    ]