# Generated by Django 4.2.1 on 2023-05-19 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0004_alter_news_link_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 9, 55, 0, 123519), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 9, 55, 0, 123519), verbose_name='Дата обновления'),
        ),
    ]
