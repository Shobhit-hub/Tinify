# Generated by Django 3.2.5 on 2022-06-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0010_alter_myurls_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myurls',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
