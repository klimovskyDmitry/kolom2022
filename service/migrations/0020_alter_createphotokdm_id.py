# Generated by Django 4.0.5 on 2022-07-22 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_alter_createphotokdm_im'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createphotokdm',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
