# Generated by Django 5.0.6 on 2024-05-24 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentform',
            name='gender',
        ),
    ]
