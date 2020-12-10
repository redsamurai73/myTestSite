# Generated by Django 3.1.2 on 2020-12-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_news_tr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('telephoneNumber', models.IntegerField()),
                ('message', models.TextField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='tr',
            field=models.TextField(default='', editable=False),
        ),
    ]
