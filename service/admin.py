from django.contrib import admin

from .models import Auto, KDM

@ admin.register (Auto)
class AutoAdmin (admin.ModelAdmin):
    list_display = ('gar', 'title', 'type')
    
@ admin.register (KDM)
class RoadwayAdmin (admin.ModelAdmin):
    list_display = ('name', 'factory', 'image')
    
