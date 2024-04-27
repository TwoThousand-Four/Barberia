from django.urls import path
from .views import home, contact, services, cart, login, register

#Para subir imagenes 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contact, name='contact'),
    path('servicios/', services, name='services'),
    path('carrito/', cart, name='cart'),
    path('login/', login, name='login'),
    path('registro/', register, name='register'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
