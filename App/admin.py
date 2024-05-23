from django.contrib import admin
from .models import Servicio, Contacto, TipoConsulta
# Register your models here.

class Homeadmin(admin.ModelAdmin):
    list_display =["id","nombre","precio"]
    search_fields = ["nombre",]
    ordering = ('-id',)
    list_per_page = 10
    list_filter =["precio"]

class Homeadmin2(admin.ModelAdmin):
    list_display = ["id", "nombre", "tipo_consulta", "mensaje"]
    search_fields= ["tipo_consulta",]
    list_per_page = 10
    list_filter=["tipo_consulta"]

admin.site.register(TipoConsulta)
admin.site.register(Servicio, Homeadmin)
admin.site.register(Contacto, Homeadmin2)

