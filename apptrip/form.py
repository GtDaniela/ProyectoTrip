from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class FormularioRegistrar(UserCreationForm):
    email = forms.EmailField(label='email',widget=forms.TextInput())
    first_name=forms.CharField(label='firts_name',widget=forms.TextInput)
    last_name=forms.CharField(label='last_name',widget=forms.TextInput)
    username=forms.CharField(label='username',widget=forms.TextInput())
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label=' Confirmar contraseña', widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['email', 'first_name','last_name','username','password1', 'password2']
        help_texts = {k:"" for k in fields }
