# Generated by Django 3.1.2 on 2020-10-27 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20201027_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 10, 21, 39, 855828, tzinfo=utc)),
        ),
    ]
