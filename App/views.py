from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'app/home.html') 

def contact (request):
    return render(request, 'app/contact.html')

def aboutUs (request):
    return render(request, 'app/aboutUs.html')

def services (request):
    return render(request, 'app/services.html')

def cart (request):
    return render(request, 'app/cart.html')