from django.shortcuts import render
from django.http import HttpResponse


def saludo(request):
    return HttpResponse("hola mundo")

# Create your views here.
