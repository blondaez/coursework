# Generated by Django 5.0.6 on 2024-06-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_service_time_service_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='date',
        ),
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.TextField(blank=True, null=True, verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='service',
            name='annotation',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='Название услуги'),
        ),
    ]
