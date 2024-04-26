from django import forms
from .models import Contacto, Servicio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


#Formulario de contacto
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]


#Formulario para agregar un servicio        
class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Servicio
        fields = '__all__'

#Formulario de registro de usuario
class RegisterForm(UserCreationForm):
    
    def clean_nombre(self):
        username =self.cleaned_data["nombre"]
        existe = User.objects.filter(username=username).exists()
        if existe:
            raise ValidationError("Ya existe un producto con ese nombre")
        return username
    
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email", "password1", "password2"]

