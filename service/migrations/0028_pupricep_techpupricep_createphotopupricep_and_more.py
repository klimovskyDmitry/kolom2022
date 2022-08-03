# Generated by Django 4.0.5 on 2022-08-03 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0027_createcommentsvpm_createphotovpm_techvpm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PUPRICEP',
            fields=[
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Марка, модель')),
                ('factory', models.CharField(max_length=100, verbose_name='Завод-изготовитель')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Фото1')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Фото2')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Фото3')),
                ('image4', models.ImageField(blank=True, upload_to='', verbose_name='Фото4')),
                ('image5', models.ImageField(blank=True, upload_to='', verbose_name='Фото5')),
                ('image6', models.ImageField(blank=True, upload_to='', verbose_name='Фото6')),
                ('image7', models.ImageField(blank=True, upload_to='', verbose_name='Фото7')),
                ('image8', models.ImageField(blank=True, upload_to='', verbose_name='Фото8')),
                ('image9', models.ImageField(blank=True, upload_to='', verbose_name='Фото9')),
                ('image10', models.ImageField(blank=True, upload_to='', verbose_name='Фото10')),
                ('tech', models.FileField(blank=True, null=True, upload_to='', verbose_name='Технические характеристики')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TechPUPRICEP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.FileField(blank=True, null=True, upload_to='', verbose_name='Технические характеристики')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.pupricep')),
            ],
        ),
        migrations.CreateModel(
            name='Createphotopupricep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото3')),
                ('im', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.pupricep')),
            ],
        ),
        migrations.CreateModel(
            name='Createcommentspupricep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.pupricep')),
            ],
        ),
    ]
