# Generated by Django 5.1.1 on 2025-02-21 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inflow',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
