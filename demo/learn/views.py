from django.shortcuts import render
from .models import Post2
# Create your views here.
def list(request):
    Data =  {'Posts': Post2.objects.all().order_by("-date")}
    return render(request, 'learn/learn.html', Data)