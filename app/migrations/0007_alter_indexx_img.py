# Generated by Django 5.0.1 on 2024-02-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_index_indexx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexx',
            name='img',
            field=models.ImageField(upload_to='places'),
        ),
    ]
