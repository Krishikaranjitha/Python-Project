# Generated by Django 5.0.6 on 2024-05-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('f_name', models.CharField(max_length=255)),
                ('m_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('gender', models.BooleanField()),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('m_no', models.CharField(max_length=255)),
            ],
        ),
    ]
