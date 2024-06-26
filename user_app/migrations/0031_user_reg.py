# Generated by Django 5.0.1 on 2024-03-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0030_delete_user_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(default='default_profile_image.jpg', upload_to='profile_images')),
                ('username', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
            ],
        ),
    ]
