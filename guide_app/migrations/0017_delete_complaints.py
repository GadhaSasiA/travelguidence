# Generated by Django 5.0.1 on 2024-03-20 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide_app', '0016_rename_email_id_guides_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Complaints',
        ),
    ]