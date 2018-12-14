from django.shortcuts import render
from .models import Post1

# Create your views here.
def list(request): 

    queryset_list=Post1.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(title__icontains=query.strip())

    data = {'Post': queryset_list.order_by("-date")}
    return render(request, 'movie/movie.html', data)


def post(request, id):
    post=Post1.objects.get(id=id)
    return render (request, 'movie/postm.html', {'post': post})