from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from service import views
# from service.views import index, navbar, roadway, kdm, pumvs, create_kdm, photo_kdm, create_photo_kdm, tech, create_comments_kdm, comments_kdm, RegisterUser
from service.views import *


urlpatterns = [
    path('service/', index),
    path ('', index, name = 'index'),
    path ('navbar/', navbar, name = 'navbar' ),
    path ('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path ('logout', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path ('register', RegisterUser.as_view(), name = 'register'),
    
    path ('roadway/', roadway, name = 'roadway'),
    path ('sidewalk/', sidewalk, name = 'sidewalk'),
    
    
    
    
    path ('kdm', kdm, name = 'kdm'),
    path ('pumvs', pumvs, name = 'pumvs'),
    path ('vpm', vpm, name = 'vpm'),
    path ('pupricep', pupricep, name = 'pupricep'),
    
    path ('trcomb', trcomb, name = 'trcomb'),
    path ('tract', tract, name = 'tract'),
    path ('trvpm', trvpm, name = 'trvpm'),
    path ('trpricep', trpricep, name = 'trpricep'),
    
    
    path ('create_kdm', create_kdm, name = 'create_kdm'),
    path ('create_photo_kdm', create_photo_kdm, name = 'create_photo_kdm'),
    path ('create_comments_kdm', create_comments_kdm, name = 'create_comments_kdm'),
    path ('photo_kdm/<int:pk>/', photo_kdm, name = 'photo_kdm'),
    path ('tech/<int:pk>/', tech, name = 'tech'),
    path ('create_tech_kdm', create_tech_kdm, name = 'create_tech_kdm'),
    path ('comments_kdm/<int:pk>/', comments_kdm, name = 'comments_kdm'),
    
    path ('create_pumvs', create_pumvs, name = 'create_pumvs'),
    path ('create_photo_pumvs', create_photo_pumvs, name = 'create_photo_pumvs'),
    path ('create_comments_pumvs', create_comments_pumvs, name = 'create_comments_pumvs'),
    path ('photo_pumvs/<int:pk>/', photo_pumvs, name = 'photo_pumvs'),
    path ('tech_pumvs/<int:pk>/', tech_pumvs, name = 'tech_pumvs'),
    path ('create_tech_pumvs', create_tech_pumvs, name = 'create_tech_pumvs'),
    path ('comments_pumvs/<int:pk>/', comments_pumvs, name = 'comments_pumvs'),
    
    path ('create_vpm', create_vpm, name = 'create_vpm'),
    path ('create_photo_vpm', create_photo_vpm, name = 'create_photo_vpm'),
    path ('create_comments_vpm', create_comments_vpm, name = 'create_comments_vpm'),
    path ('photo_vpm/<int:pk>/', photo_vpm, name = 'photo_vpm'),
    path ('tech_vpm/<int:pk>/', tech_vpm, name = 'tech_vpm'),
    path ('create_tech_vpm', create_tech_vpm, name = 'create_tech_vpm'),
    path ('comments_vpm/<int:pk>/', comments_vpm, name = 'comments_vpm'),
    
    path ('create_pupricep', create_pupricep, name = 'create_pupricep'),
    path ('create_photo_pupricep', create_photo_pupricep, name = 'create_photo_pupricep'),
    path ('create_comments_pupricep', create_comments_pupricep, name = 'create_comments_pupricep'),
    path ('photo_pupricep/<int:pk>/', photo_pupricep, name = 'photo_pupricep'),
    path ('tech_pupricep/<int:pk>/', tech_pupricep, name = 'tech_pupricep'),
    path ('create_tech_pupricep', create_tech_pupricep, name = 'create_tech_pupricep'),
    path ('comments_pupricep/<int:pk>/', comments_pupricep, name = 'comments_pupricep'),
    
    path ('create_trcomb', create_trcomb, name = 'create_trcomb'),
    path ('create_photo_trcomb', create_photo_trcomb, name = 'create_photo_trcomb'),
    path ('create_comments_trcomb', create_comments_trcomb, name = 'create_comments_trcomb'),
    path ('photo_trcomb/<int:pk>/', photo_trcomb, name = 'photo_trcomb'),
    path ('tech_trcomb/<int:pk>/', tech_trcomb, name = 'tech_trcomb'),
    path ('create_tech_trcomb', create_tech_trcomb, name = 'create_tech_trcomb'),
    path ('comments_trcomb/<int:pk>/', comments_trcomb, name = 'comments_trcomb'),
    
    path ('create_tract', create_tract, name = 'create_tract'),
    path ('create_photo_tract', create_photo_tract, name = 'create_photo_tract'),
    path ('create_comments_ttract', create_comments_tract, name = 'create_comments_tract'),
    path ('photo_tract/<int:pk>/', photo_tract, name = 'photo_tract'),
    path ('tech_tract/<int:pk>/', tech_tract, name = 'tech_tract'),
    path ('create_tech_tract', create_tech_tract, name = 'create_tech_tract'),
    path ('comments_tract/<int:pk>/', comments_tract, name = 'comments_tract'),
    
    path ('create_trvpm', create_trvpm, name = 'create_trvpm'),
    path ('create_photo_trvpm', create_photo_trvpm, name = 'create_photo_trvpm'),
    path ('create_comments_ttrvpm', create_comments_trvpm, name = 'create_comments_trvpm'),
    path ('photo_trvpm/<int:pk>/', photo_trvpm, name = 'photo_trvpm'),
    path ('tech_trvpm/<int:pk>/', tech_trvpm, name = 'tech_trvpm'),
    path ('create_tech_trvpm', create_tech_trvpm, name = 'create_tech_trvpm'),
    path ('comments_trvpm/<int:pk>/', comments_trvpm, name = 'comments_trvpm'),
    
    
    
]