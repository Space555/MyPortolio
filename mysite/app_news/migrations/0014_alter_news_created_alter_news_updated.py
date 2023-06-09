# Generated by Django 4.2.1 on 2023-06-08 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0013_alter_news_category_new_alter_news_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 14, 1, 21, 494371), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 14, 1, 21, 494371), verbose_name='Дата обновления'),
        ),
    ]
