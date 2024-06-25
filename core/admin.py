from django.contrib import admin
from .models import *
#Importacion para admin
from django.contrib.admin import ModelAdmin
from admin_confirm import AdminConfirmMixin
# Register your models here.

class EmpleadoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['rut', 'nombre', 'apellido', 'edad']


admin.site.register(TipoEmpleado)
admin.site.register(Empleado, EmpleadoModelAdmin)
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Mecanico_servicio)
