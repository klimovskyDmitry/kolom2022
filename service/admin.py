from django.contrib import admin

# from .models import Auto, KDM, PUMVS, VPM, PUPRICEP, Createphotokdm, Createcommentskdm, TechKDM
from .models import *

@ admin.register (Auto)
class AutoAdmin (admin.ModelAdmin):
    list_display = ('gar', 'title', 'type')
    
@ admin.register (KDM)
class KDMAdmin (admin.ModelAdmin):
    list_display = ('name', 'chassis', 'factory', 'image', 'tech', 'comment', 'id')

@ admin.register (Createphotokdm)
class CreatephotokdmAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentskdm)
class CreatecommentskdmAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechKDM)
class TechKDMAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  

@ admin.register (PUMVS)
class PUMVSAdmin (admin.ModelAdmin):
    list_display = ('name', 'chassis', 'factory', 'image', 'tech', 'comment', 'id')

@ admin.register (Createphotopumvs)
class CreatephotopumvsAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentspumvs)
class CreatecommentspumvsAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechPUMVS)
class TechPUMVSAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  
    
@ admin.register (VPM)
class VPMAdmin (admin.ModelAdmin):
    list_display = ('name', 'chassis', 'factory', 'image', 'tech', 'comment', 'id')
    
@ admin.register (Createphotovpm)
class CreatephotovpmAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentsvpm)
class CreatecommentsvpmAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechVPM)
class TechVPMAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  
    
@ admin.register (PUPRICEP)
class PUPRICEPAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image', 'tech', 'comment', 'id')
    
@ admin.register (Createphotopupricep)
class CreatephotopupricepAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentspupricep)
class CreatecommentspupricepAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechPUPRICEP)
class TechPUPRICEPAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  