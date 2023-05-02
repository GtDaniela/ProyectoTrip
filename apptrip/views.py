from django.shortcuts import render
from .models import *
from apptrip import form
from apptrip.form import *
from django.contrib.auth.decorators import login_required
# from .forms import FormularioRegistrar
# Create your views here.

def registrarse(request):
    mensaje=""
    print(str("entra"))
    if request.method == 'POST':
        print(str("entra if 1"))
        #la linea siguiente es la que comunica el form.py con los datos cogidos del input del html
        # form = FormularioRegistrar(request.POST)
        #coger datos del formulario del html
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password1= request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(str(email)+""+str(first_name)+""+str(last_name))
        print(str(password1)+""+str(password2))
        usuario=User()
        usuario.email=email
        usuario.first_name=first_name
        usuario.last_name=last_name
        usuario.username=username
        usuario.password=password1
        # usuario.save()
        # commit=true asegura que los datos se guarden sincronizados carga pereso
        if password1==password2:
            usuario.save()
            usuario1=User.objects.all().last()
            idusuario=int(usuario1.id)
            viajero=Viajero()
            viajero.user_id=int(idusuario)
            viajero.alias=username
            viajero.save()
        else:
            mensaje="ERROR EN CONTRASEÑA"

    #     if form.is_valid():
    #         print(str("entra if 2"))
    #         request.user.is_staff=False
    #         #request.user.is_active=False para indicar que el usuario no está registrado hasta que confirme el email
    #         #request.user.is_superuser=False
    #
    #         #commit actualiza cuando toodo está finalizado
    #         username = form.cleaned_data['username']
    #         # messages.success(request, f'Usuario {username} creado')
    #         return redirect('register.html')
    # else:
    #     form = FormularioRegistrar()
    context = { 'form' : form , 'mensaje':mensaje}
    return render(request, 'register.html', context)


def inicio(request):
    return render (request,'inicio.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(str(username)+str(password))
    if request.method== 'GET':
        return render(request,'login.html')
    return render (request,'inicio.html')

def logout(request):#cogemos el usuario activo
    username=request.user.username
    password=request.user.password
    user=authenticate(request,username=username,password=password)
    # logout(request)
    return render (request,'register.html')