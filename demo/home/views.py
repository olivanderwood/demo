from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
   return render(request, 'pages/home.html')
def games(request):
    return render(request, 'pages/games.html')
def movie(request):
    return render(request, 'pages/movie.html')
def learn(request):
    return render(request, 'pages/learn.html')
def faqs(request):
    return render(request, 'pages/faqs.html')