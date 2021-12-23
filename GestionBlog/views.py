from django.shortcuts import render,HttpResponse
from GestionBlog.models import Post

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog.html", {"posts": posts}) 
    """{"posts": posts} deben ser iguales, de lo contrario no funciona"""