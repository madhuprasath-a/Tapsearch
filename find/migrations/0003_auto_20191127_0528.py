# Generated by Django 2.2.7 on 2019-11-27 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0002_unique_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unique',
            old_name='unique',
            new_name='word',
        ),
    ]
