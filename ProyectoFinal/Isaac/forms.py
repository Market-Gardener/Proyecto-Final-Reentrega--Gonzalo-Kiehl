from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()
    
class FormularioItems(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()