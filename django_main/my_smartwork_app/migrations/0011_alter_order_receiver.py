# Generated by Django 5.0.4 on 2024-05-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_smartwork_app', '0010_remove_order_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Receiver',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]