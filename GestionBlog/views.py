from django.shortcuts import render,HttpResponse
from GestionBlog.models import Post, Categoria

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog.html", {"posts": posts}) 
    """{"posts": posts} deben ser iguales, de lo contrario no funciona"""

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "categorias.html", {'categoria':categoria, "posts": posts })