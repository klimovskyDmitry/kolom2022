from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from service import views
from service.views import index, navbar, roadway, kdm, pumvs, create_kdm, photo_kdm, RegisterForm


urlpatterns = [
    path('service/', index),
    path ('', index, name = 'index'),
    path ('navbar/', navbar, name = 'navbar' ),
    path ('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path ('logout', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path ('register', views.RegisterForm.as_view(), name = 'register'),
    
    path ('roadway/', roadway, name = 'roadway'),
    path ('kdm', kdm, name = 'kdm'),
    path ('pumvs', pumvs, name = 'pumvs'),
    path ('create_kdm', create_kdm, name = 'create_kdm'),
    path ('photo_kdm/<int:pk>/', photo_kdm, name = 'photo_kdm'),
    
]