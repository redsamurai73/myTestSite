# Generated by Django 3.1.2 on 2020-10-22 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='news',
            name='publishedDate',
        ),
        migrations.RemoveField(
            model_name='news',
            name='rubric',
        ),
        migrations.AddField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 8, 57, 31, 940899, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
