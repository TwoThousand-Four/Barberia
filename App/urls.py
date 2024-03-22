from django.urls import path
from .views import home, contact, aboutUs

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contact, name='contact'),
    path('nosotros/', aboutUs, name='aboutUs'),
    
]