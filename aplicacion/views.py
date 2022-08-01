from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from aplicacion.models import Curso


def saludo(request):
    return HttpResponse("hola mundo")

def saludo_a(request, nombre):
    return HttpResponse(f"hola como estas {nombre.capitalize()}")

def saludo_personalizado(request):
    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]

    return render(request, "aplicacion/index.html", context)

def lista_cursos(request):
    context ={}

    context["cursos"] = Curso.objects.all()
    return render(request, "aplicacion/lista_cursos.html", context)

    

# Create your views here.
