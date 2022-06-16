# Generated by Django 4.0.5 on 2022-06-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='gar',
            field=models.PositiveSmallIntegerField(verbose_name='Гар.№'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Марка, модель'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Тип'),
        ),
    ]
