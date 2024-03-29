# Generated by Django 5.0.1 on 2024-02-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_photo', models.ImageField(upload_to='placeimage')),
                ('Your_name', models.CharField(max_length=200)),
                ('place_name', models.CharField(max_length=200)),
                ('about_place', models.TextField(max_length=400)),
                ('opinion', models.TextField(max_length=500)),
            ],
        ),
    ]
