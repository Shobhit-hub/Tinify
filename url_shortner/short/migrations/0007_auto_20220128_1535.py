# Generated by Django 3.2.5 on 2022-01-28 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0006_alter_myurls_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('comments', models.CharField(max_length=5000)),
            ],
        ),
        migrations.AlterField(
            model_name='myurls',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 28, 15, 35, 2, 203053)),
        ),
    ]
