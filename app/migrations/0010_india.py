# Generated by Django 5.0.1 on 2024-02-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_popular_delete_indexx'),
    ]

    operations = [
        migrations.CreateModel(
            name='india',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='densinations1')),
                ('placename', models.CharField(max_length=100)),
                ('about_place', models.TextField(max_length=400)),
                ('place_features', models.TextField(max_length=100)),
            ],
        ),
    ]