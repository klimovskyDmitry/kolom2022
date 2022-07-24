from django.contrib import admin

from .models import Auto, KDM, PUMVS, VPM, PUPRICEP, Createphotokdm

@ admin.register (Auto)
class AutoAdmin (admin.ModelAdmin):
    list_display = ('gar', 'title', 'type')
    
@ admin.register (KDM)
class KDMAdmin (admin.ModelAdmin):
    list_display = ('name', 'chassis', 'factory', 'image', 'tech', 'comment', 'id')

@ admin.register (Createphotokdm)
class CreatephotokdmAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')    

    
@ admin.register (PUMVS)
class PUMVSAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image')
    
@ admin.register (VPM)
class VPMAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image')
    
@ admin.register (PUPRICEP)
class PUPRICEPAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image')