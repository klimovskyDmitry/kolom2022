from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect, render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import KDM, PUMVS, VPM, PUPRICEP
from .forms import KdmForm
from django.forms import modelform_factory


def index (req):
    return render (req, 'index.html')

def navbar (req):
    return render (req, 'navbar.html')


def roadway (req):
    return render (req, 'for_roadway.html')

def kdm (req):
    all_kdms = {'kdms' : KDM.objects.all()}
    return render (req, 'kdm.html', all_kdms)

def pumvs (req):
    all_pumvss = {'pumvss' : PUMVS.objects.all()}
    return render (req, 'pumvs.html', all_pumvss)

def photo_kdm (req):
    return render (req, 'for_roadway.html')

def create_kdm (req):
    kdm_form = KdmForm()
    if req.method == "POST":
        kdm_form = KdmForm(req.POST)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('kdm')
    return render (req, 'kdm_form.html', {'form': kdm_form})
   