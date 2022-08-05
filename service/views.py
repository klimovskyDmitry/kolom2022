from itertools import count
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import KDM, PUMVS, VPM, Createphotokdm, Createcommentskdm, Createphotopumvs, Createcommentspumvs
from .models import *
# from .forms import RegisterUserForm, KdmForm, CreatephotokdmForm, CreatecommentskdmForm, TechkdmForm
from .forms import *
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
    
# Для ограничения доступа незарегистрированным к for_.......
@login_required
def roadway (req):
    return render (req, 'for_roadway.html')

@login_required
def sidewalk (req):
    return render (req, 'for_sidewalk.html')


    
    
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
    return render (req, 'pumvs.html', {'pumvss' : PUMVS.objects.all()})

def vpm (req):
    return render (req, 'vpm.html', {'vpms' : VPM.objects.all()})

def pupricep (req):
    return render (req, 'pupricep.html', {'pupriceps' : PUPRICEP.objects.all()})

def trcomb (req):
    return render (req, 'trcomb.html',{'trcombs' : TRCOMB.objects.all()})

def tract (req):
    return render (req, 'tract.html',{'tracts' : TRACT.objects.all()})

def trvpm (req):
    return render (req, 'trvpm.html',{'trvpms' : TRVPM.objects.all()})

def trpricep (req):
    return render (req, 'trpricep.html',{'trpriceps' : TRPRICEP.objects.all()})






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

def create_tech_kdm (req):
    kdm = TechkdmForm()
    if req.method == "POST":
        kdm = TechkdmForm(req.POST,req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('kdm')
    return render (req, 'kdm_form.html', {'form': kdm})

def comments_kdm (req, pk):    
    kdm = get_object_or_404(KDM, pk=pk)
    a = Createcommentskdm.objects.filter(name=kdm.pk)
    b = User.objects.all()
    return render(req, 'comments/kdm_comments.html', {'kdm': kdm, 'a':a, 'b':b})

def create_kdm (req):
    kdm_form = KdmForm()
    if req.method == "POST":
        kdm_form = KdmForm(req.POST, req.FILES)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('kdm')
    return render (req, 'kdm_form.html', {'form': kdm_form})

def photo_pumvs (req, pk):    
    kdm = get_object_or_404(PUMVS, pk=pk)
    a = Createphotopumvs.objects.filter(im=kdm.pk)
    return render(req, 'photo/pumvs_gallery.html', {'pumvs': kdm, 'a':a})

def create_photo_pumvs (req):
    kdm = CreatephotopumvsForm()
    if req.method == "POST":
        kdm = CreatephotopumvsForm(req.POST, req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('pumvs')
    return render (req, 'kdm_form.html', {'form': kdm})

def create_comments_pumvs (req):
    kdm = CreatecommentspumvsForm()
    if req.method == "POST":
        kdm = CreatecommentspumvsForm(req.POST)
        if kdm.is_valid():
            kdm.save()
            return redirect ('pumvs')
    return render (req, 'kdm_form.html', {'form': kdm})


def tech_pumvs (req, pk):    
    kdm = get_object_or_404(PUMVS, pk=pk)
    return render(req, 'tech/pumvs_tech.html', {'pumvs': kdm})

def create_tech_pumvs (req):
    kdm = TechpumvsForm()
    if req.method == "POST":
        kdm = TechpumvsForm(req.POST,req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('pumvs')
    return render (req, 'kdm_form.html', {'form': kdm})

def comments_pumvs (req, pk):    
    pumvs = get_object_or_404(PUMVS, pk=pk)
    a = Createcommentspumvs.objects.filter(name=pumvs.pk)
    b = User.objects.all()
    return render(req, 'comments/pumvs_comments.html', {'pumvs': pumvs, 'a':a, 'b':b})

def create_pumvs (req):
    kdm_form = PumvsForm()
    if req.method == "POST":
        kdm_form = PumvsForm(req.POST, req.FILES)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('pumvs')
    return render (req, 'kdm_form.html', {'form': kdm_form})

def photo_vpm (req, pk):    
    kdm = get_object_or_404(VPM, pk=pk)
    a = Createphotovpm.objects.filter(im=kdm.pk)
    return render(req, 'photo/vpm_gallery.html', {'vpm': kdm, 'a':a})

def create_photo_vpm (req):
    kdm = CreatephotovpmForm()
    if req.method == "POST":
        kdm = CreatephotovpmForm(req.POST, req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('vpm')
    return render (req, 'kdm_form.html', {'form': kdm})

def create_comments_vpm (req):
    kdm = CreatecommentsvpmForm()
    if req.method == "POST":
        kdm = CreatecommentsvpmForm(req.POST)
        if kdm.is_valid():
            kdm.save()
            return redirect ('vpm')
    return render (req, 'kdm_form.html', {'form': kdm})


def tech_vpm (req, pk):    
    kdm = get_object_or_404(VPM, pk=pk)
    return render(req, 'tech/vpm_tech.html', {'vpm': kdm})

def create_tech_vpm (req):
    kdm = TechvpmForm()
    if req.method == "POST":
        kdm = TechvpmForm(req.POST,req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('vpm')
    return render (req, 'kdm_form.html', {'form': kdm})

def comments_vpm (req, pk):    
    vpm = get_object_or_404(VPM, pk=pk)
    a = Createcommentsvpm.objects.filter(name=vpm.pk)
    b = User.objects.all()
    return render(req, 'comments/vpm_comments.html', {'vpm': vpm, 'a':a, 'b':b})

def create_vpm (req):
    kdm_form = VpmForm()
    if req.method == "POST":
        kdm_form = VpmForm(req.POST, req.FILES)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('vpm')
    return render (req, 'kdm_form.html', {'form': kdm_form})
   
def photo_pupricep (req, pk):    
    kdm = get_object_or_404(PUPRICEP, pk=pk)
    a = Createphotopupricep.objects.filter(im=kdm.pk)
    return render(req, 'photo/pupricep_gallery.html', {'pupricep': kdm, 'a':a})

def create_photo_pupricep (req):
    kdm = CreatephotopupricepForm()
    if req.method == "POST":
        kdm = CreatephotopupricepForm(req.POST, req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('pupricep')
    return render (req, 'kdm_form.html', {'form': kdm})

def create_comments_pupricep (req):
    kdm = CreatecommentspupricepForm()
    if req.method == "POST":
        kdm = CreatecommentspupricepForm(req.POST)
        if kdm.is_valid():
            kdm.save()
            return redirect ('pupricep')
    return render (req, 'kdm_form.html', {'form': kdm})


def tech_pupricep (req, pk):    
    kdm = get_object_or_404(PUPRICEP, pk=pk)
    return render(req, 'tech/pupricep_tech.html', {'pupricep': kdm})

def create_tech_pupricep (req):
    kdm = TechpupricepForm()
    if req.method == "POST":
        kdm = TechpupricepForm(req.POST,req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('pupricep')
    return render (req, 'kdm_form.html', {'form': kdm})

def comments_pupricep (req, pk):    
    pupricep = get_object_or_404(PUPRICEP, pk=pk)
    a = Createcommentspupricep.objects.filter(name=pupricep.pk)
    b = User.objects.all()
    return render(req, 'comments/pupricep_comments.html', {'pupricep': pupricep, 'a':a, 'b':b})

def create_pupricep (req):
    kdm_form = PupricepForm()
    if req.method == "POST":
        kdm_form = PupricepForm(req.POST, req.FILES)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('pupricep')
    return render (req, 'kdm_form.html', {'form': kdm_form})

def photo_trcomb (req, pk):    
    kdm = get_object_or_404(TRCOMB, pk=pk)
    a = Createphototrcomb.objects.filter(im=kdm.pk)
    return render(req, 'photo/trcomb_gallery.html', {'trcomb': kdm, 'a':a})

def create_photo_trcomb (req):
    kdm = CreatephototrcombForm()
    if req.method == "POST":
        kdm = CreatephototrcombForm(req.POST, req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trcomb')
    return render (req, 'kdm_form.html', {'form': kdm})

def create_comments_trcomb (req):
    kdm = CreatecommentstrcombForm()
    if req.method == "POST":
        kdm = CreatecommentstrcombForm(req.POST)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trcomb')
    return render (req, 'kdm_form.html', {'form': kdm})


def tech_trcomb (req, pk):    
    kdm = get_object_or_404(TRCOMB, pk=pk)
    return render(req, 'tech/trcomb_tech.html', {'trcomb': kdm})

def create_tech_trcomb (req):
    kdm = TechtrcombForm()
    if req.method == "POST":
        kdm = TechtrcombForm(req.POST,req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trcomb')
    return render (req, 'kdm_form.html', {'form': kdm})

def comments_trcomb (req, pk):    
    kdm = get_object_or_404(TRCOMB, pk=pk)
    a = Createcommentstrcomb.objects.filter(name=kdm.pk)
    b = User.objects.all()
    return render(req, 'comments/trcomb_comments.html', {'trcomb': kdm, 'a':a, 'b':b})

def create_trcomb (req):
    kdm_form = TrcombForm()
    if req.method == "POST":
        kdm_form = TrcombForm(req.POST, req.FILES)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('trcomb')
    return render (req, 'kdm_form.html', {'form': kdm_form})

def photo_tract (req, pk):    
    kdm = get_object_or_404(TRACT, pk=pk)
    a = Createphototract.objects.filter(im=kdm.pk)
    return render(req, 'photo/tract_gallery.html', {'tract': kdm, 'a':a})

def create_photo_tract (req):
    kdm = CreatephototractForm()
    if req.method == "POST":
        kdm = CreatephototractForm(req.POST, req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('tract')
    return render (req, 'kdm_form.html', {'form': kdm})

def create_comments_tract (req):
    kdm = CreatecommentstractForm()
    if req.method == "POST":
        kdm = CreatecommentstractForm(req.POST)
        if kdm.is_valid():
            kdm.save()
            return redirect ('tract')
    return render (req, 'kdm_form.html', {'form': kdm})


def tech_tract (req, pk):    
    kdm = get_object_or_404(TRACT, pk=pk)
    return render(req, 'tech/tract_tech.html', {'tract': kdm})

def create_tech_tract (req):
    kdm = TechtractForm()
    if req.method == "POST":
        kdm = TechtractForm(req.POST,req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('tract')
    return render (req, 'kdm_form.html', {'form': kdm})

def comments_tract (req, pk):    
    kdm = get_object_or_404(TRACT, pk=pk)
    a = Createcommentstract.objects.filter(name=kdm.pk)
    b = User.objects.all()
    return render(req, 'comments/tract_comments.html', {'tract': kdm, 'a':a, 'b':b})

def create_tract (req):
    kdm_form = TractForm()
    if req.method == "POST":
        kdm_form = TractForm(req.POST, req.FILES)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('tract')
    return render (req, 'kdm_form.html', {'form': kdm_form})

def photo_trvpm (req, pk):    
    kdm = get_object_or_404(TRVPM, pk=pk)
    a = Createphototrvpm.objects.filter(im=kdm.pk)
    return render(req, 'photo/trvpm_gallery.html', {'trvpm': kdm, 'a':a})

def create_photo_trvpm (req):
    kdm = CreatephototrvpmForm()
    if req.method == "POST":
        kdm = CreatephototrvpmForm(req.POST, req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trvpm')
    return render (req, 'kdm_form.html', {'form': kdm})

def create_comments_trvpm (req):
    kdm = CreatecommentstrvpmForm()
    if req.method == "POST":
        kdm = CreatecommentstrvpmForm(req.POST)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trvpm')
    return render (req, 'kdm_form.html', {'form': kdm})


def tech_trvpm (req, pk):    
    kdm = get_object_or_404(TRVPM, pk=pk)
    return render(req, 'tech/trvpm_tech.html', {'trvpm': kdm})

def create_tech_trvpm (req):
    kdm = TechtrvpmForm()
    if req.method == "POST":
        kdm = TechtrvpmForm(req.POST,req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trvpm')
    return render (req, 'kdm_form.html', {'form': kdm})

def comments_trvpm (req, pk):    
    kdm = get_object_or_404(TRVPM, pk=pk)
    a = Createcommentstrvpm.objects.filter(name=kdm.pk)
    b = User.objects.all()
    return render(req, 'comments/trvpm_comments.html', {'trvpm': kdm, 'a':a, 'b':b})

def create_trvpm (req):
    kdm_form = TrvpmForm()
    if req.method == "POST":
        kdm_form = TrvpmForm(req.POST, req.FILES)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('trvpm')
    return render (req, 'kdm_form.html', {'form': kdm_form})

def photo_trpricep (req, pk):    
    kdm = get_object_or_404(TRPRICEP, pk=pk)
    a = Createphototrpricep.objects.filter(im=kdm.pk)
    return render(req, 'photo/trpricep_gallery.html', {'trpricep': kdm, 'a':a})

def create_photo_trpricep (req):
    kdm = CreatephototrpricepForm()
    if req.method == "POST":
        kdm = CreatephototrpricepForm(req.POST, req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trpricep')
    return render (req, 'kdm_form.html', {'form': kdm})

def create_comments_trpricep (req):
    kdm = CreatecommentstrpricepForm()
    if req.method == "POST":
        kdm = CreatecommentstrpricepForm(req.POST)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trpricep')
    return render (req, 'kdm_form.html', {'form': kdm})


def tech_trpricep (req, pk):    
    kdm = get_object_or_404(TRPRICEP, pk=pk)
    return render(req, 'tech/trpricep_tech.html', {'trpricep': kdm})

def create_tech_trpricep (req):
    kdm = TechtrpricepForm()
    if req.method == "POST":
        kdm = TechtrpricepForm(req.POST,req.FILES)
        if kdm.is_valid():
            kdm.save()
            return redirect ('trpricep')
    return render (req, 'kdm_form.html', {'form': kdm})

def comments_trpricep (req, pk):    
    kdm = get_object_or_404(TRPRICEP, pk=pk)
    a = Createcommentstrpricep.objects.filter(name=kdm.pk)
    b = User.objects.all()
    return render(req, 'comments/trpricep_comments.html', {'trpricep': kdm, 'a':a, 'b':b})

def create_trpricep (req):
    kdm_form = TrpricepForm()
    if req.method == "POST":
        kdm_form = TrpricepForm(req.POST, req.FILES)
        if kdm_form.is_valid():
            kdm_form.save()
            return redirect ('trpricep')
    return render (req, 'kdm_form.html', {'form': kdm_form})
