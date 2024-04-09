# Generated by Django 5.0.1 on 2024-03-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0018_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=254)),
                ('Password1', models.CharField(max_length=100)),
                ('Password2', models.CharField(max_length=100)),
            ],
        ),
    ]
