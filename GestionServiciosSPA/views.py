from django.shortcuts import render, HttpResponse
#Llamando la clase servivio que esta en GestionServiciosSPA
from GestionServiciosSPA.models import Servicio 
# Create your views here.



def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, "servicios.html", {"servicios": servicios})