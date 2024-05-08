from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import ContactForm, RegisterForm, ServiceForm
from django.contrib import messages
from .models import Servicio
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

#Inicio
def home (request):
    return render(request, 'app/home.html') 

#Contacto
def contact (request):
    return render(request, 'app/contact.html')

#Servicios
def services (request):
    servicios = Servicio.objects.all()
    return render(request, 'app/services.html', {'servicios':servicios})

#Carrito
def cart (request):
    return render(request, 'app/cart.html')

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

#Login
def logIn(request):
    return render(request, 'accounts/login.html')

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

#Agregar Servicio
@permission_required('app.add_servicio')
def add (request):
    data = {
        'form': ServiceForm()
    }
    if request.method == 'POST':
        formulario = ServiceForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio agregado correctamente")
        else:
            data['form'] = formulario
    return render(request, 'app/crud/add.html', data)

#Listar
@permission_required('app.view_servicio')
def list(request):
    servicios = Servicio.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(servicios, 5)
        servicios = paginator.page(page)
    except:
        raise Http404
    
    data={
        'entity':servicios,
        'paginator':paginator
    }
    return render(request, 'app/crud/list.html', data)

#Modificar
@permission_required('app.change_servicio')
def modify(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    data = {
        'form': ServiceForm(instance=servicio)
    }    
    if request.method == 'POST':
        formulario = ServiceForm(data=request.POST,instance=servicio ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio modficado correctamente")
            return redirect(to="list")
        else:
            data['form'] = formulario
    return render(request, 'app/crud/modify.html', data)

#Eliminar
@permission_required('app.delete_servicio')
def delete(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    messages.success(request, "Servicio eliminado correctamente")
    return redirect(to="list")