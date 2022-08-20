from django.urls import path # funcion para manejar las url
from . import views  # se importa todo lo que esta dentro de el archivo views, como funciones y otros atributos. El punto significa que todo lo que esta en el archivo views lo traigo desde la carpeta que estoy actualmente, como es la carpeta home.

urlpatterns = [
    path('', views.index, name='index'), # como hay coincidencia en la ruta vacia entonces ejecuta la funcion index  que esta en el arcivo views. El name= index es el monbre que le doy a la urls. 
]
