# Generated by Django 3.2.18 on 2023-04-06 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='email',
            field=models.CharField(default=22, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stdymtrls',
            name='pid',
            field=models.ForeignKey(default=1234, on_delete=django.db.models.deletion.CASCADE, to='sign.parent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tips',
            name='pid',
            field=models.ForeignKey(default=2334, on_delete=django.db.models.deletion.CASCADE, to='sign.parent'),
            preserve_default=False,
        ),
    ]