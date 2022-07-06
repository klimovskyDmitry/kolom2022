from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import KDM, PUMVS, VPM, PUPRICEP


def index (req):
    return render (req, 'index.html')

def navbar (req):
    return render (req, 'navbar.html')

def photo (req):
    return render (req, 'photo.html')

def roadway (req):
    return render (req, 'for_roadway.html')

def kdm (req):
    all_kdms = {'kdms' : KDM.objects.all()}
    return render (req, 'kdm.html', all_kdms)

def pumvs (req):
    all_pumvss = {'pumvss' : PUMVS.objects.all()}
    return render (req, 'pumvs.html', all_pumvss)
   