from django import forms

class Formulariocontacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True, max_length=50)
    email=forms.CharField(label="Email", required=True, max_length=50)
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)