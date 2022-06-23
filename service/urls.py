from django.contrib import admin
from django.urls import path
from service.views import index, navbar, photo


urlpatterns = [
    path('service/', index),
    path ('', index, name = 'index'),
    path ('navbar/', navbar, name = 'navbar' ),
    path ('photo/', photo, name = 'photo'),
]