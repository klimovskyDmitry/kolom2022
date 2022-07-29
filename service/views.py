from itertools import count
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm

from .models import KDM, PUMVS, VPM, PUPRICEP, Createphotokdm, Createcommentskdm
from .forms import RegisterUserForm, KdmForm, CreatephotokdmForm, CreatecommentskdmForm
from django.forms import modelform_factory, modelformset_factory
from logging.config import IDENTIFIER
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



class RegisterUser (SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    success_message = "%(username)s успешно зарегистрирован"
    template_name = 'register.html'
    success_url = reverse_lazy ('index')
    
# Для ограничения доступа незарегистрированным к for_roadway.html
@login_required
def roadway (req):
    return render (req, 'for_roadway.html')




    
    
# class PostView (LoginRequiredMixin, ListView):
#     login_url = 'login'
#     model = KDM
#     template_name = "index.html"



def index (req):
     return render (req, 'index.html')

def navbar (req):
    return render (req, 'navbar.html')


def kdm (req):
    
    return render (req, 'kdm.html',{'kdms' : KDM.objects.all()})

def pumvs (req):
    all_pumvss = {'pumvss' : PUMVS.objects.all()}
    return render (req, 'pumvs.html', all_pumvss)

def photo_kdm (req, pk):    
    kdm = get_object_or_404(KDM, pk=pk)
    a = Createphotokdm.objects.filter(im=kdm.pk)
   
    return render(req, 'photo/kdm_gallery.html', {'kdm': kdm, 'a':a})

def create_photo_kdm (req):
    kdm = CreatephotokdmForm()
    if req.method == "POST":
        kdm = CreatephotokdmForm(req.POST, req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('kdm')
    return render (req, 'kdm_form.html', {'form': kdm})

def create_comments_kdm (req):
    kdm = CreatecommentskdmForm()
    if req.method == "POST":
        kdm = CreatecommentskdmForm(req.POST)
        if kdm.is_valid():
            kdm.save()
            return redirect ('kdm')
    return render (req, 'kdm_form.html', {'form': kdm})



def tech (req, pk):    
    kdm = get_object_or_404(KDM, pk=pk)
    return render(req, 'tech/kdm_tech.html', {'kdm': kdm})




def comments_kdm (req, pk):    
    kdm = get_object_or_404(KDM, pk=pk)
    a = Createcommentskdm.objects.filter(name=kdm.pk)
    return render(req, 'comments/kdm_comments.html', {'kdm': kdm, 'a':a})



def create_kdm (req):
    kdm_form = KdmForm()
    if req.method == "POST":
        kdm_form = KdmForm(req.POST, req.FILES)
    
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('kdm')
    return render (req, 'kdm_form.html', {'form': kdm_form})
   