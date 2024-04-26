from django.contrib import admin
from .models import Servicio, Contacto
# Register your models here.

class Homeadmin(admin.ModelAdmin):
    list_display =["id","nombre","precio"]
    search_fields = ["nombre","tipo",]
    ordering = ('-id',)
    list_per_page = 10

class Homeadmin2(admin.ModelAdmin):
    list_display = ["id", "nombre", "tipo_consulta"]
    search_fields= ["tipo_consulta",]
    list_per_page = 10

admin.site.register(Servicio, Homeadmin)
admin.site.register(Contacto, Homeadmin2)

