# Generated by Django 4.2.3 on 2023-07-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_auto_20230711_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='link',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
