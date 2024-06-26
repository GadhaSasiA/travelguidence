# Generated by Django 5.0.1 on 2024-03-06 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_travelguide'),
        ('guide_app', '0010_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('Select_india_destinations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.india')),
                ('Select_kerala_destinations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.kerala')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.guide')),
                ('select_Popular_destinations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.popular')),
            ],
        ),
    ]
