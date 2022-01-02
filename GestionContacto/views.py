from django.shortcuts import render,HttpResponse
from django.forms import formu

from forms import FormularioconFormulariocontacto

# Create your views here.
def contacto(request):

    return render(request, "contacto.html")