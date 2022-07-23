# Generated by Django 3.2.5 on 2022-07-05 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0011_alter_myurls_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imp_urls',
            name='url',
        ),
        migrations.AddField(
            model_name='imp_urls',
            name='uid',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_feedback',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
