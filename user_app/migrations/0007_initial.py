# Generated by Django 5.0.1 on 2024-03-05 13:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0022_travelguide'),
        ('user_app', '0006_remove_favorite_destination_remove_favorite_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('Select_india_destinations', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.india')),
                ('Select_kerala_destinations', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.kerala')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.guide')),
                ('select_Popular_destinations', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.popular')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
