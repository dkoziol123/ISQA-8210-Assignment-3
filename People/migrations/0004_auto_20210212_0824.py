# Generated by Django 2.2 on 2021-02-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0003_auto_20210212_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.IntegerField(max_length=50),
        ),
    ]
