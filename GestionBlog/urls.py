from django.urls import path
from GestionBlog import views

#configuracion para media
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

   path('blog/', views.blog, name="Blog"), #quitar blog/ si da error
   path('blog/categoria/<categoria_id>/', views.categoria, name="Categoria"), #colocar int:<> si da error mas luego


]

#Configuracion acceso a direcion carpeta media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



