# Generated by Django 5.0.1 on 2024-03-04 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_guide_remove_travelguide_user_name'),
        ('guide_app', '0008_alter_bookinginfo_guide'),
        ('user_app', '0005_alter_booking_guide'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TravelGuide',
        ),
    ]
