# Generated by Django 5.1.5 on 2025-02-10 04:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_hiddengem_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activty',
            new_name='Activity',
        ),
    ]
