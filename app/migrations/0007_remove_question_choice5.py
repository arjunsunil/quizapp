# Generated by Django 2.0.3 on 2018-03-10 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180310_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='Choice5',
        ),
    ]
