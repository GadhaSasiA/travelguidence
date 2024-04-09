# Generated by Django 5.0.1 on 2024-03-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide_app', '0021_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='guide_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='guides',
        ),
    ]