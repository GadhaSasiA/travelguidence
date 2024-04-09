# Generated by Django 5.0.1 on 2024-04-04 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide_app', '0029_direct_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct_message',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='guide_app.guide_reg'),
        ),
    ]
