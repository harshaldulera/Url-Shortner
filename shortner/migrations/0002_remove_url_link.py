# Generated by Django 4.2.3 on 2023-07-11 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='link',
        ),
    ]
