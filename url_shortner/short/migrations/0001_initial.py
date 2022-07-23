# Generated by Django 3.2.5 on 2021-12-03 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imp_urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
                ('target', models.CharField(max_length=1000)),
                ('username', models.CharField(default='null', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='myurls',
            fields=[
                ('url', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('date', models.DateField(default=datetime.datetime(2021, 12, 3, 20, 56, 45, 212366))),
                ('uid', models.CharField(default='jj', max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]