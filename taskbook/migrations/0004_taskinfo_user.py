# Generated by Django 4.2 on 2023-08-11 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskbook', '0003_alter_userinfo_username_alter_taskinfo_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskinfo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskbook.userinfo'),
        ),
    ]