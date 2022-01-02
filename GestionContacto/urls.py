from django.urls import path
from GestionContacto import views

#configuracion para media
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('contacto/', views.contacto, name="Contacto"),

]

