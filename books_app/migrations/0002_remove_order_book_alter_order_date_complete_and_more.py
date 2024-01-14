# Generated by Django 4.2.5 on 2024-01-06 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
        migrations.AlterField(
            model_name='order',
            name='date_complete',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 6, 19, 42, 4, 596313, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_formation',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата формирования'),
        ),
        migrations.AlterField(
            model_name='order',
            name='execution_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Время выполнения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='services',
            field=models.ManyToManyField(blank=True, null=True, to='books_app.service', verbose_name='Работы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Введён'), (2, 'В работе'), (3, 'Завершён'), (4, 'Отменён'), (5, 'Удалён')], default=1, verbose_name='Статус'),
        ),
    ]
