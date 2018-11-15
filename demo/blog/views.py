from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.
def list( request ):
    queryset_list=Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(Q(title__icontains=query.strip())) 

    data = {'Posts': queryset_list.order_by("-date")}
    return render (request, 'blog/blog.html', data)

def post(request, id):
    post=Post.objects.get(id=id)
    return render (request, 'blog/post.html', {'post': post})

