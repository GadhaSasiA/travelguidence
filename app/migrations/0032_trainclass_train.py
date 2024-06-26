# Generated by Django 5.0.1 on 2024-03-22 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_class', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_place', models.CharField(max_length=100)),
                ('to_place', models.CharField(max_length=100)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('select_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainclass')),
            ],
        ),
    ]
