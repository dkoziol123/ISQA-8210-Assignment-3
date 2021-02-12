# Generated by Django 2.2 on 2021-02-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Selection', '0005_auto_20210212_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='Budget_Dollar',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='selection',
            name='Time_Frame_Hour',
            field=models.IntegerField(max_length=48),
        ),
    ]