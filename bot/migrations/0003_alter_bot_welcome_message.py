# Generated by Django 4.1.1 on 2022-10-09 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='welcome_message',
            field=models.TextField(default='Welcome: <django.db.models.query_utils.DeferredAttribute object at 0x7f8783be9ed0> !!!'),
        ),
    ]