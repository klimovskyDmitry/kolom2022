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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
    
class Createphotokdm (models.Model):
    im = models.ForeignKey("KDM", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentskdm (models.Model):
    name = models.ForeignKey("KDM", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechKDM (models.Model):
    name = models.ForeignKey("KDM", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    
    
class PUMVS (models.Model):
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class Createphotopumvs (models.Model):
    im = models.ForeignKey("PUMVS", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentspumvs (models.Model):
    name = models.ForeignKey("PUMVS", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechPUMVS (models.Model):
    name = models.ForeignKey("PUMVS", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    
class VPM (models.Model):
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class Createphotovpm (models.Model):
    im = models.ForeignKey("VPM", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentsvpm (models.Model):
    name = models.ForeignKey("VPM", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechVPM (models.Model):
    name = models.ForeignKey("VPM", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    
class PUPRICEP (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class Createphotopupricep (models.Model):
    im = models.ForeignKey("PUPRICEP", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentspupricep (models.Model):
    name = models.ForeignKey("PUPRICEP", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechPUPRICEP (models.Model):
    name = models.ForeignKey("PUPRICEP", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)  
    
class TRCOMB (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class Createphototrcomb (models.Model):
    im = models.ForeignKey("TRCOMB", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentstrcomb (models.Model):
    name = models.ForeignKey("TRCOMB", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechTRCOMB (models.Model):
    name = models.ForeignKey("TRCOMB", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)     
    
class TRACT (models.Model):
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class Createphototract (models.Model):
    im = models.ForeignKey("TRACT", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentstract (models.Model):
    name = models.ForeignKey("TRACT", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechTRACT (models.Model):
    name = models.ForeignKey("TRACT", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)     
    
class TRVPM (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class Createphototrvpm (models.Model):
    im = models.ForeignKey("TRVPM", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentstrvpm (models.Model):
    name = models.ForeignKey("TRVPM", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechTRVPM (models.Model):
    name = models.ForeignKey("TRVPM", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)     
    
class TRPRICEP (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class Createphototrpricep (models.Model):
    im = models.ForeignKey("TRPRICEP", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentstrpricep (models.Model):
    name = models.ForeignKey("TRPRICEP", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechTRPRICEP (models.Model):
    name = models.ForeignKey("TRPRICEP", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)     
    
class FP (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class Createphotofp (models.Model):
    im = models.ForeignKey("FP", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class Createcommentsfp (models.Model):
    name = models.ForeignKey("FP", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechFP (models.Model):
    name = models.ForeignKey("FP", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True) 
    
class SNOWLOADER (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class CreatephotoSL (models.Model):
    im = models.ForeignKey("SNOWLOADER", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class CreatecommentsSL (models.Model):
    name = models.ForeignKey("SNOWLOADER", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechSL (models.Model):
    name = models.ForeignKey("SNOWLOADER", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)  
    
class GRADER (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class CreatephotoGR (models.Model):
    im = models.ForeignKey("GRADER", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class CreatecommentsGR (models.Model):
    name = models.ForeignKey("GRADER", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechGR (models.Model):
    name = models.ForeignKey("GRADER", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    
class BULLDOZER (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class CreatephotoBU (models.Model):
    im = models.ForeignKey("BULLDOZER", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class CreatecommentsBU (models.Model):
    name = models.ForeignKey("BULLDOZER", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechBU (models.Model):
    name = models.ForeignKey("BULLDOZER", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True) 
    
class SNOWMELTING (models.Model):
    name = models.CharField (verbose_name='Марка, модель', max_length=50, unique=True)
    
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
        
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)
    comment = models.TextField (verbose_name= 'Комментарии', null = True, blank=True)
    id = models.IntegerField(primary_key=True)
    
    def __str__ (self):
        return self.name
    
class CreatephotoSM (models.Model):
    im = models.ForeignKey("SNOWMELTING", null=True, on_delete=models.CASCADE)
    image1 = models.ImageField (verbose_name= 'Фото1', null=True, blank=True)
    image2 = models.ImageField (verbose_name= 'Фото2', null=True, blank=True)
    image3 = models.ImageField (verbose_name= 'Фото3', null=True, blank=True)

class CreatecommentsSM (models.Model):
    name = models.ForeignKey("SNOWMELTING", null=True, on_delete=models.CASCADE)
    comment = models.TextField (verbose_name= 'Комментарий', null = True, blank=True)
    
class TechSM (models.Model):
    name = models.ForeignKey("SNOWMELTING", null=True, on_delete=models.CASCADE)
    tech = models.FileField (verbose_name= 'Технические характеристики',null = True, blank=True)                                 