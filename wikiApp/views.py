from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'vistaPrincipal.html')

def nuevoTema(request):
    return render(request,'nuevoTema.html')

def nuevoArticulo(request):
    return render(request,'nuevoArticulo.html')

def Ingeniería(request):
    return render(request,'Ingeniería.html')

def Informática(request):
    return render(request,'Informática.html')

def Economía(request):
    return render(request,'Economía.html')

def Derecho(request):
    return render(request,'Derecho.html')

def articulos11(request):
    return render(request,'articulos11.html')

def articulos12(request):
    return render(request,'articulos12.html')

def articulos21(request):
    return render(request,'articulos21.html')

def articulos22(request):
    return render(request,'articulos22.html')

def articulos31(request):
    return render(request,'articulos31.html')

def articulos32(request):
    return render(request,'articulos32.html')

def articulos41(request):
    return render(request,'articulos41.html')

def articulos42(request):
    return render(request,'articulos42.html')

def busqueda(request):
    return render(request,'busqueda.html')