# Generated by Django 3.2.18 on 2023-04-10 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20230406_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stdymtrls',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='tips',
            name='pid',
        ),
    ]
