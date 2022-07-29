from django import forms
from django.forms import fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import KDM, Createphotokdm, Createcommentskdm


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
        fields = ['name', 'chassis', 'factory', 'image', 'image1', 'image2', 'image3','image4','image5','image6','tech', 'comment', ]
        
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
        