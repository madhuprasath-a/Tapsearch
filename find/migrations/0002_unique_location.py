# Generated by Django 2.2.7 on 2019-11-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unique',
            name='location',
            field=models.ManyToManyField(blank=True, to='find.Para'),
        ),
    ]
