from django.shortcuts import render,HttpResponse
#from Zoe_Beauty_Spa.GestionContacto.forms import Formulariocontacto

from .forms import Formulariocontacto

# Create your views here.
def contacto(request):
    formulario_contacto=Formulariocontacto()
    return render(request, "contacto.html", {'miFormulario':formulario_contacto})