# Generated by Django 2.2 on 2021-02-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0004_auto_20210212_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.BigIntegerField(max_length=50),
        ),
    ]
