import uuid
from django.db import models
from django.core import validators
from django.contrib.auth.models import User

class Auto (models.Model):
    id = models.IntegerField (primary_key=True)
    gar = models.CharField (verbose_name='Гар.№', max_length=5)
    title = models.CharField (verbose_name='Марка, модель', max_length=100)
    type = models.CharField (verbose_name='Тип', max_length=100)

class KDM (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    chassis = models.CharField (verbose_name='Шасси', max_length=50, blank=True)
    factory = models.CharField (verbose_name='Завод-изготовитель', max_length=100)
    image = models.ImageField (verbose_name= 'Фото')
    image1 = models.ImageField (verbose_name= 'Фото1', blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', blank=True)
    image4 = models.ImageField (verbose_name= 'Фото4', blank=True)
    image5 = models.ImageField (verbose_name= 'Фото5', blank=True)
    image6 = models.ImageField (verbose_name= 'Фото6', blank=True)
    image7 = models.ImageField (verbose_name= 'Фото7', blank=True)
    image8 = models.ImageField (verbose_name= 'Фото8', blank=True)
    image9 = models.ImageField (verbose_name= 'Фото9', blank=True)
    image10 = models.ImageField (verbose_name= 'Фото10', blank=True)
        
    tech = models.TextField (verbose_name= 'Технические характеристики', blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', blank=True)
    id = models.IntegerField(primary_key=True)
    
    
class Createphotokdm (models.Model):
    im = models.ForeignKey("KDM", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)
    
    
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
    
