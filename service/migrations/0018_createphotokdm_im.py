# Generated by Django 4.0.5 on 2022-07-22 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_createphotokdm_alter_kdm_image1_alter_kdm_image10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='createphotokdm',
            name='im',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='service.kdm'),
            preserve_default=False,
        ),
    ]
