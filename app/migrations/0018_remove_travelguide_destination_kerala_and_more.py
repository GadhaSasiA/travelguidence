# Generated by Django 5.0.1 on 2024-02-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_india_img_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelguide',
            name='destination_kerala',
        ),
        migrations.RemoveField(
            model_name='travelguide',
            name='destination_popular',
        ),
        migrations.AlterField(
            model_name='travelguide',
            name='guide_image',
            field=models.ImageField(upload_to='guidephoto'),
        ),
    ]
