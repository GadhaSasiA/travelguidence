# Generated by Django 5.0.1 on 2024-03-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=100)),
                ('phonenum', models.IntegerField()),
                ('address', models.TextField()),
                ('booking_date_time', models.DateTimeField()),
                ('Travel_date', models.DateTimeField()),
            ],
        ),
    ]
