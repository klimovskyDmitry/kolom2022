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