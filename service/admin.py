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
    
@ admin.register (TRCOMB)
class TRCOMBAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image', 'tech', 'comment', 'id')
    
@ admin.register (Createphototrcomb)
class CreatephototrcombAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentstrcomb)
class CreatecommentstrcombAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechTRCOMB)
class TechTRCOMBAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  

@ admin.register (TRACT)
class TRACTAdmin (admin.ModelAdmin):
    list_display = ('name', 'chassis', 'factory', 'image', 'tech', 'comment', 'id')
    
@ admin.register (Createphototract)
class CreatephototractAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentstract)
class CreatecommentstractAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechTRACT)
class TechTRACTAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  
    
@ admin.register (TRVPM)
class TRVPMAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image', 'tech', 'comment', 'id')
    
@ admin.register (Createphototrvpm)
class CreatephototrvpmAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentstrvpm)
class CreatecommentstrvpmAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechTRVPM)
class TechTRVPMAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  
    
@ admin.register (TRPRICEP)
class TRPRICEPAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image', 'tech', 'comment', 'id')
    
@ admin.register (Createphototrpricep)
class CreatephototrpricepAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentstrpricep)
class CreatecommentstrpricepAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechTRPRICEP)
class TechTRPRICEPAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  
    
@ admin.register (FP)
class FPAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image', 'tech', 'comment', 'id')
    
@ admin.register (Createphotofp)
class CreatephotofpAdmin (admin.ModelAdmin):
    list_display = ('im', 'image1', 'image2', 'image3')
    
@ admin.register (Createcommentsfp)
class CreatecommentsfpAdmin (admin.ModelAdmin):
    list_display = ('name', 'comment')   
    
@ admin.register (TechFP)
class TechFPAdmin (admin.ModelAdmin):
    list_display = ('name', 'tech')  