from django.shortcuts import render

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