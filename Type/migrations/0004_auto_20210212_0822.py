# Generated by Django 2.2 on 2021-02-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Type', '0003_auto_20210212_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='Private',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='type',
            name='Public',
            field=models.CharField(max_length=3),
        ),
    ]
