from hashlib import new
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import LoginForm 
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def login_view(request):
    form = LoginForm() ## formulario para loguearse. 
    if request.method == 'POST':  # se la pregunta si es un post. Si no lo es se pasa todo el cuerpo del if y se retorna el formulario para loguearse.  
        form = LoginForm(request.POST)
        if form.is_valid(): # si los caracteres que se ingresa son validos. 
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:    # retorna un usuario real, si es asi se le redirecciona a una pagina 'index'.
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Credenciales inválidas')
        else:
            messages.error(request, 'Hay errores en el formulario')
    return render(request, 'accounts/login.html', {'form': form})


## Deslogueamos al usuario. 
def logout_view(request):
    logout(request) 
    return redirect('index') #A donde queremos que se diriga una vez que se cierra sesion. 


def registrar_usuario(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, f'Usuario {new_user.username} creado!')
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form}) ##Aqui FALTA
 

