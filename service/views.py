from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render


def index (req):
    return render (req, 'index.html')

def navbar (req):
    return render (req, 'navbar.html')

def photo (req):
    return render (req, 'photo.html')