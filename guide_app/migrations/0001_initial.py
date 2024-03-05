# Generated by Django 5.0.1 on 2024-02-22 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0015_travelguide'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=10)),
                ('Select_destinations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.popular')),
                ('Select_destinationskerala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kerala')),
                ('select_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.travelguide')),
            ],
        ),
    ]