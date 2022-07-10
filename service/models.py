from django.db import models

class Auto (models.Model):
    id = models.IntegerField (primary_key=True)
    gar = models.CharField (verbose_name='Гар.№', max_length=5)
    title = models.CharField (verbose_name='Марка, модель', max_length=100)
    type = models.CharField (verbose_name='Тип', max_length=100)

class KDM (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50)
    chassis = models.CharField (verbose_name='Шасси', max_length=50, blank=True)
    factory = models.CharField (verbose_name='Завод-изготовитель', max_length=100)
    image = models.ImageField (verbose_name= 'Фото', blank=True)
    tech = models.TextField (verbose_name= 'Технические характеристики', blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', blank=True)
    
class PUMVS (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50)
    factory = models.CharField (verbose_name='Завод-изготовитель', max_length=100)
    image = models.ImageField (verbose_name= 'Фото')
    
class VPM (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50)
    factory = models.CharField (verbose_name='Завод-изготовитель', max_length=100)
    image = models.ImageField (verbose_name= 'Фото')
    
class PUPRICEP (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50)
    factory = models.CharField (verbose_name='Завод-изготовитель', max_length=100)
    image = models.ImageField (verbose_name= 'Фото')