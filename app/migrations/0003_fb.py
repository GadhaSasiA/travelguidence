# Generated by Django 5.0.1 on 2024-02-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_mail_from_mail_from_id_rename_mailto_mail_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='fb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_userid', models.CharField(max_length=100)),
                ('fb_password', models.CharField(max_length=100)),
            ],
        ),
    ]
