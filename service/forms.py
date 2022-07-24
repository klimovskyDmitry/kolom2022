from django import forms
from django.forms import fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import KDM, Createphotokdm


class UserRegisterForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
    


class KdmForm (forms.ModelForm):
    class Meta:
        model = KDM
        fields = ['name', 'chassis', 'factory', 'image', 'image1', 'image2', 'image3','image4','image5','image6', 'comment' ]
        # widgets = {'name':widgets.Textarea}

class CreatephotokdmForm (forms.ModelForm):
    class Meta:
        model = Createphotokdm
        fields = ['im', 'image1', 'image2', 'image3' ]
        