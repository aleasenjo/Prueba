from .models import Gato
from django import forms

class GatoForm(forms.ModelForm):
    

    class Meta:
        model = Gato
        fields = (
            'fotografia',
            'nombre',
            'descripcion'
        )
        labels = {
            'fotografia':'Fotografia',
            'nombre':'Nombre',
            'descripcion':'Descripcion del gato'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
        }
