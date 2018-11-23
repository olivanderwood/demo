from django.shortcuts import render
from .models import Post1
# Create your views here.
def list(request): 
    data={'Post': Post1.objects.all().order_by("-date")}
    return render(request, 'movie/movie.html', data)