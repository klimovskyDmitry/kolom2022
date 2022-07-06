from django.contrib import admin
from django.urls import path
from service.views import index, navbar, photo, roadway, kdm, pumvs


urlpatterns = [
    path('service/', index),
    path ('', index, name = 'index'),
    path ('navbar/', navbar, name = 'navbar' ),
    path ('photo/', photo, name = 'photo'),
    path ('roadway/', roadway, name = 'roadway'),
    path ('kdm', kdm, name = 'kdm'),
    path ('pumvs', pumvs, name = 'pumvs'),
]