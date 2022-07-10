from django.contrib import admin
from django.urls import path
from service.views import index, navbar, roadway, kdm, pumvs, create_kdm


urlpatterns = [
    path('service/', index),
    path ('', index, name = 'index'),
    path ('navbar/', navbar, name = 'navbar' ),
    
    path ('roadway/', roadway, name = 'roadway'),
    path ('kdm', kdm, name = 'kdm'),
    path ('pumvs', pumvs, name = 'pumvs'),
    path ('create_kdm', create_kdm, name = 'create_kdm'),
    
]