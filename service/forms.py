from django import forms
from django.forms import fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import KDM, Createphotokdm, Createcommentskdm, TechKDM, KDM, Createphotokdm, Createcommentskdm, TechKDM
from .models import *

class RegisterUserForm (UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }
    
class KdmForm (forms.ModelForm):
    class Meta:
        model = KDM
        fields = ['name', 'chassis', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotokdmForm (forms.ModelForm):
    class Meta:
        model = Createphotokdm
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentskdmForm (forms.ModelForm):
    class Meta:
        model = Createcommentskdm
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechkdmForm (forms.ModelForm):
    class Meta:
        model = TechKDM
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class PumvsForm (forms.ModelForm):
    class Meta:
        model = PUMVS
        fields = ['name', 'chassis', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotopumvsForm (forms.ModelForm):
    class Meta:
        model = Createphotopumvs
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentspumvsForm (forms.ModelForm):
    class Meta:
        model = Createcommentspumvs
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechpumvsForm (forms.ModelForm):
    class Meta:
        model = TechPUMVS
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class VpmForm (forms.ModelForm):
    class Meta:
        model = VPM
        fields = ['name', 'chassis', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotovpmForm (forms.ModelForm):
    class Meta:
        model = Createphotovpm
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentsvpmForm (forms.ModelForm):
    class Meta:
        model = Createcommentsvpm
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechvpmForm (forms.ModelForm):
    class Meta:
        model = TechVPM
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class PupricepForm (forms.ModelForm):
    class Meta:
        model = PUPRICEP
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotopupricepForm (forms.ModelForm):
    class Meta:
        model = Createphotopupricep
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentspupricepForm (forms.ModelForm):
    class Meta:
        model = Createcommentspupricep
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechpupricepForm (forms.ModelForm):
    class Meta:
        model = TechPUPRICEP
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class TrcombForm (forms.ModelForm):
    class Meta:
        model = TRCOMB
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephototrcombForm (forms.ModelForm):
    class Meta:
        model = Createphototrcomb
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentstrcombForm (forms.ModelForm):
    class Meta:
        model = Createcommentstrcomb
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechtrcombForm (forms.ModelForm):
    class Meta:
        model = TechTRCOMB
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class TractForm (forms.ModelForm):
    class Meta:
        model = TRACT
        fields = ['name', 'chassis', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephototractForm (forms.ModelForm):
    class Meta:
        model = Createphototract
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentstractForm (forms.ModelForm):
    class Meta:
        model = Createcommentstract
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechtractForm (forms.ModelForm):
    class Meta:
        model = TechTRACT
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class TrvpmForm (forms.ModelForm):
    class Meta:
        model = TRVPM
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephototrvpmForm (forms.ModelForm):
    class Meta:
        model = Createphototrvpm
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentstrvpmForm (forms.ModelForm):
    class Meta:
        model = Createcommentstrvpm
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechtrvpmForm (forms.ModelForm):
    class Meta:
        model = TechTRVPM
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class TrpricepForm (forms.ModelForm):
    class Meta:
        model = TRPRICEP
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephototrpricepForm (forms.ModelForm):
    class Meta:
        model = Createphototrpricep
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentstrpricepForm (forms.ModelForm):
    class Meta:
        model = Createcommentstrpricep
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechtrpricepForm (forms.ModelForm):
    class Meta:
        model = TechTRPRICEP
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class FPForm (forms.ModelForm):
    class Meta:
        model = FP
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotofpForm (forms.ModelForm):
    class Meta:
        model = Createphotofp
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentsfpForm (forms.ModelForm):
    class Meta:
        model = Createcommentsfp
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechfpForm (forms.ModelForm):
    class Meta:
        model = TechFP
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class SLForm (forms.ModelForm):
    class Meta:
        model = SNOWLOADER
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotoSLForm (forms.ModelForm):
    class Meta:
        model = CreatephotoSL
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentsSLForm (forms.ModelForm):
    class Meta:
        model = CreatecommentsSL
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechSLForm (forms.ModelForm):
    class Meta:
        model = TechSL
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class GRForm (forms.ModelForm):
    class Meta:
        model = GRADER
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotoGRForm (forms.ModelForm):
    class Meta:
        model = CreatephotoGR
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentsGRForm (forms.ModelForm):
    class Meta:
        model = CreatecommentsGR
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechGRForm (forms.ModelForm):
    class Meta:
        model = TechGR
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class BUForm (forms.ModelForm):
    class Meta:
        model = BULLDOZER
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotoBUForm (forms.ModelForm):
    class Meta:
        model = CreatephotoBU
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentsBUForm (forms.ModelForm):
    class Meta:
        model = CreatecommentsBU
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechBUForm (forms.ModelForm):
    class Meta:
        model = TechBU
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}
        
class SMForm (forms.ModelForm):
    class Meta:
        model = SNOWMELTING
        fields = ['name', 'factory', 'image', 'image1', 'image2', 'image3', 'tech', 'comment', ]
        
        # widgets = {'name':widgets.Textarea}

class CreatephotoSMForm (forms.ModelForm):
    class Meta:
        model = CreatephotoSM
        fields = ['im', 'image1', 'image2', 'image3', ]
        labels = {"im" : 'Выберите марку'}
        
class CreatecommentsSMForm (forms.ModelForm):
    class Meta:
        model = CreatecommentsSM
        fields = ['name', 'comment', ]
        labels = {"name" : 'Выберите марку'}
        
class TechSMForm (forms.ModelForm):
    class Meta:
        model = TechSM
        fields = ['name', 'tech', ]
        labels = {"name" : 'Выберите марку'}