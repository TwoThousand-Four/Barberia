from django.urls import path
from .views import home, contact, services, cart

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contact, name='contact'),
    path('servicios/', services, name='services'),
    path('carrito/', cart, name='cart'),
    
]