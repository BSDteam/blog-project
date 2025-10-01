from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")

def about(request):
    return HttpResponse("<h1>Добро пожаловать не туда!</h1>")