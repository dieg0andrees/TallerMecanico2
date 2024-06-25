from django.urls import include, path
from .views import *
from rest_framework import routers

#CONFIGURACIÖN PARA API
router = routers.DefaultRouter()
router.register('tipoempleados', TipoEmpleadoViewset)
router.register('empleados', EmpleadoViewset)

urlpatterns = [

    path('',index, name="index"),
    path('empleados/',empleados, name="empleados"),
    path('contact/',contact, name="contact"),
    path('consultas/',listar_consultas, name="consulta"),
    path('about/',about, name="about"),
    path('aceites/',aceites, name="aceites"),
    path('apis/',apis, name="apis"),
    path('marcas/',marcas, name="marcas"),
    path('booking/',servicios_y_mecanicos, name="booking"),
    path('testimonial/',testimonial, name="testimonial"),
    path('technicians/',technicians, name="technicians"),
    path('resumenpago/',resumen_pedido, name="resumenpago"),
    path('empleados/add/',empleadosadd, name="empleadosadd"),
    path('empleados/update/<id>/',empleadosupdate, name="empleadosupdate"),
    path('empleados/delete/<id>/',empleadosdelete, name="empleadosdelete"),
    path('accounts/',include('django.contrib.auth.urls')),
    
    #path('services/',servicios, name="servicios"),
    #path('services/', mecanicos, name="servicios"),
    path('services/', verservicio, name="verservicios"),
    path('salir/',salir,name="salir"),
    path('register/', register, name="register"),
    #api
    path('api/', include(router.urls)),
    path('empleadosapi/',empleadosapi, name="empleadosapi"),
    #TIPO EMPLEADOS
    path('tipoempleados/',tipoempleados, name="tipoempleados"),
    path('tipoempleados/add/',tipoempleadosadd, name="tipoempleadosadd"),
    path('tipoempleados/update/<id>/',tipoempleadosupdate, name="tipoempleadosupdate"),
    path('tipoempleados/delete/<id>/',tipoempleadosdelete, name="tipoempleadosdelete"),
    #SERVICIOS
    path('servicios/',servicios, name="servicios"),
    path('servicios/add/',serviciosadd, name="serviciosadd"),
    path('servicios/update/<id>/',serviciosupdate, name="serviciosupdate"),
    path('servicios/delete/<id>/',serviciosdelete, name="serviciosdelete"),
    path('account_locked/',account_locked, name = "account_locked"),
    path('captcha/', include('captcha.urls')),
    path('pago_servicio/',pago_servicio, name="pago_servicio"),
    path('confirmacion_pago/', confirmacion_pago, name='confirmacion_pago'),
    path('descargar_boleta/', descargar_boleta, name='descargar_boleta'),
    
]
