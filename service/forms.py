from django import forms

from .models import KDM

class KdmForm (forms.ModelForm):
    class Meta:
        model = KDM
        fields = '__all__'

