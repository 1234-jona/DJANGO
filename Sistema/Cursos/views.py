from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html')
def curso(request):
    cursos=Curso.objects.all()
    print(cursos)
    return render(request,'cursos/index.html',{'cursos':cursos})
def crear(request):
    return render(request,'cursos/crear.html')
def editar(request):
    return render(request,'cursos/editar.html')
