# Generated by Django 2.2 on 2021-02-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0002_auto_20210211_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={},
        ),
        migrations.RemoveField(
            model_name='people',
            name='publish',
        ),
    ]
