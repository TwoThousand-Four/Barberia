from django.urls import path
from .views import home, contact, aboutUs, services, cart

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contact, name='contact'),
    path('nosotros/', aboutUs, name='aboutUs'),
    path('servicios/', services, name='services'),
    path('carrito/', cart, name='cart'),
    
]