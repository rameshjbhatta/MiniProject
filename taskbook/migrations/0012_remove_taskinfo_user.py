# Generated by Django 4.2 on 2023-08-24 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskbook', '0011_alter_taskinfo_timedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskinfo',
            name='user',
        ),
    ]
