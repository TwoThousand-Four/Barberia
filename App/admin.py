from django.contrib import admin
from .models import TipoServicio, Servicio, Contacto
# Register your models here.

class Homeadmin(admin.ModelAdmin):
    list_display =["id","tipo","precio",]
    list_editable = ["precio"]
    search_fields = ["tipo"]
    ordering = ('-id',)
    list_filter = ('tipo',)
    list_per_page = 10
    
class Homeadmin2(admin.ModelAdmin):
    list_display =["id","nombre","tipo","precio"]
    search_fields = ["nombre","tipo",]
    ordering = ('-id',)
    list_per_page = 10

class Homeadmin3(admin.ModelAdmin):
    list_display = ["id", "nombre", "tipo_consulta"]
    search_fields= ["tipo_consulta",]
    list_per_page = 10
    
class Homeadmin4(admin.ModelAdmin):
    list_display =["id","nombre",]
    search_fields = ["nombre",]
    ordering = ('-id',)
    list_per_page = 10

admin.site.register(TipoServicio, Homeadmin)
admin.site.register(Servicio, Homeadmin2)
admin.site.register(Contacto, Homeadmin3)

