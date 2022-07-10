# Generated by Django 4.0.5 on 2022-07-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_kdm_chassis_alter_kdm_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='kdm',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарии'),
        ),
        migrations.AddField(
            model_name='kdm',
            name='tech',
            field=models.TextField(blank=True, verbose_name='Технические характеристики'),
        ),
    ]
