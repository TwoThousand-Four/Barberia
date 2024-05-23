from django.urls import path
from .views import home, contact, services, reserve, logIn, register, add, list, modify, delete, add_service, delete_service, subtract_service, clean_cart
                

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
    path('añadir/<int:servicio_id>/', add_service, name="add_service"),
    path('borrar/<int:servicio_id>/', delete_service, name="delete_service"),
    path('restar/<int:servicio_id>/', subtract_service, name="subtract_service"),
    path('limpiar/', clean_cart, name="clean_cart"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
