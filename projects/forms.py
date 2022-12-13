from django.forms import ModelForm
from .models import Contacto
from django import forms
from django.forms import TextInput, EmailInput, Textarea 


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={
                'class': "input-control i-c-2",
                'placeholder': 'Nombre'
                }),
            'mail': EmailInput(attrs={
                'class': "input-control i-c-2", 
                'placeholder': 'Correo'
                }),
            'titulo': TextInput(attrs={
                'class': "input-control",
                'placeholder': '¿Qué tienes que decirnos?'
                }),
            'contenido': Textarea(attrs={
                'class': "input-control",
                'placeholder': 'Escribe aquí tu mensaje'
                })
            
        }
        
