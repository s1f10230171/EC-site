# Generated by Django 2.2.28 on 2025-01-10 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20250110_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='address',
            new_name='adress',
        ),
    ]
