# Generated by Django 4.2.1 on 2023-05-22 04:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0007_alter_imagenews_news_alter_news_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img_news/%Y/%m/%d/', verbose_name='Фото новостей'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 10, 10, 42, 401426), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 10, 10, 42, 401426), verbose_name='Дата обновления'),
        ),
        migrations.DeleteModel(
            name='ImageNews',
        ),
    ]
