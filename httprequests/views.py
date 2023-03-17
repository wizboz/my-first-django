from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'httprequests/home.html')

def hello(request):
    return HttpResponse('<h1 style="color:blue;">hello lalalalala</h1>')