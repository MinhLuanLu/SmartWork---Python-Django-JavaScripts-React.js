# Generated by Django 5.0.4 on 2024-05-16 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_smartwork_app', '0015_alter_user_join_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Join_Datetime',
        ),
    ]
