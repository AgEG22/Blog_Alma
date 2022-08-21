from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm): ## se esta extendiendo el formulario que viene por defecto 
    class Meta:                     ## en la clase meta se va a indicar el usuario. 
        model = User
        fields = ['username', 'password1', 'password2']        ## aqui va otro campo fields. 