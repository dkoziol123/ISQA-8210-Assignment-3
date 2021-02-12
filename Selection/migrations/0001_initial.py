# Generated by Django 2.2 on 2021-02-12 00:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
