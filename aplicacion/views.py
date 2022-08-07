from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from aplicacion.models import Curso
from aplicacion.forms import formulario


def saludo(request):
    return HttpResponse("hola mundo")

def saludo_a(request, nombre):
    return HttpResponse(f"hola como estas {nombre.capitalize()}")

#def saludo_personalizado(request):
    #context = {}

    #if request.GET:
    #    context["nombre"] = request.GET["nombre"]

    #return render(request, "aplicacion/index.html", context)

#def lista_cursos(request):
    #context ={}

    #context["cursos"] = Curso.objects.all()
    #return render(request, "aplicacion/models", context)

def mostrar_index(request):
    return render (request, "aplicacion/index_nuevo.html", {})
    
def index(request):
    return render (request, "aplicacion/index.html",{})

def home(request):
    return render (request, "aplicacion/home.html",{})

def lista_curso(request):
    return render (request, "aplicacion/lista_cursos.html",{})

def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario = formulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            curso = Curso (nombre=informacion['nombre'], camada=informacion['camada'])

            curso.save()

            return render(request, "aplicacion/home.html")
        pass
    else:

        miFormulario= formulario()

        return render(request, "aplicacion/cursoformulario.html", {"miFormulario":miFormulario})


# Create your views here.
