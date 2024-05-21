from django.urls import path
from .views import home, contact, services, reserve, logIn, register, add, list, modify, delete, create_payment, ejecutarPago, cancelarPago
#Para subir imagenes 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contact, name='contact'),
    path('servicios/', services, name='services'),
    path('agendar/', reserve, name='reserve'),
    path('login/', logIn, name='login'),
    path('registro/', register, name='register'),
    path('agregar/', add, name="add"),   
    path('listar/', list, name="list"),   
    path('modificar/<id>/', modify, name="modify"),   
    path('eliminar/<id>/', delete, name="delete"), 

    path('payment/create', create_payment, name='create_payment'),
    path('payment/execute', ejecutarPago, name='execute_payment'),
    path('payment/cancel', cancelarPago, name='cancel_payment'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
