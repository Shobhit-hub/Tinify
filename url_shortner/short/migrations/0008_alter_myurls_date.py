# Generated by Django 3.2.5 on 2022-06-25 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0007_auto_20220128_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myurls',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 25, 17, 57, 20, 944673, tzinfo=utc)),
        ),
    ]
