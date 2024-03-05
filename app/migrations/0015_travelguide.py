# Generated by Django 5.0.1 on 2024-02-22 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_travelguide'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_image', models.ImageField(upload_to='guidepic')),
                ('guide_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('destination_kerala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kerala')),
                ('destination_popular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.popular')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.userprofile')),
            ],
        ),
    ]
