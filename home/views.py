from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html') #la funcion render lo que hace es renderizarme el html. 
