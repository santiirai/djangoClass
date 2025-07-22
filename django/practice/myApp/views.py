from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    return HttpResponse("<h1>Hellooooo</h1>")

def index(request):
    return render(request, "index.html")
  

def about(request):
    return render(request, "about.html")

# Create your views here.
