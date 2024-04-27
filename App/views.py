from django.shortcuts import render, redirect

from .forms import ContactForm, RegisterForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

# Create your views here.

#Inicio
def home (request):
    return render(request, 'app/home.html') 

#Contacto
def contact (request):
    return render(request, 'app/contact.html')

#Servicios
def services (request):
    return render(request, 'app/services.html')

#Carrito
def cart (request):
    return render(request, 'app/cart.html')

#Login
def login(request):
    return render(request, 'accounts/login.html')

#Registro
def register(request):
    data = {
        'form':RegisterForm
    }
    if request.method == 'POST':
        formulario = RegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro exitoso!")
            return redirect(to='home')
        else:
            data['form'] = formulario
    return render(request, 'registration/register.html', data)

#Contacto
def contact(request):
    data = {
        'form': ContactForm()
    }
    if request.method == 'POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Formulario enviado")
        else:
            data['form'] = formulario
    return render(request, 'app/contact.html', data)