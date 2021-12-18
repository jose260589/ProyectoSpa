from django.urls import path
from GestionServiciosSPA import views

#configuracion para media
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('servicios/', views.servicios, name="Servicios"),

]

#Configuracion acceso a direcion carpeta media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)