from django.http import HttpResponseBadRequest
from django.shortcuts import render,redirect
from django.urls import reverse
import requests
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib import messages
##API



def empleadosapi(request):
    response = requests.get('http://127.0.0.1:8000/api/empleados/')
    response2 = requests.get('https://digimon-api.vercel.app/api/digimon')
    empleados = response.json()
    digimon = response2.json()

    paginator = Paginator(digimon, 10) #Nos muestra 10 digimons x página
    page_number = request.GET.get('page') #Busca la página
    page_obj = paginator.get_page(page_number)

    aux = {
        'lista' : empleados,
        'page_obj' : page_obj
    }
    return render(request,'core/empleados/crudapi/index.html', aux)

class TipoEmpleadoViewset(viewsets.ModelViewSet):
    queryset = TipoEmpleado.objects.all()
    serializer_class = TipoEmpleadoSerializer
    renderer_classes = [JSONRenderer]

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    renderer_classes = [JSONRenderer]

def account_locked(request):
     return render(request,'core/account_locked.html')

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def contact(request):
    return render(request,'core/contact.html')

#def services(request):
#    return render(request,'core/services.html')

def about(request):
    return render(request,'core/about.html')

def booking(request):
    return render(request,'core/booking.html')

def testimonial(request):
    return render(request,'core/testimonial.html')

def technicians(request):
    return render(request,'core/technicians.html')

def aceites(request):
    return render(request,'core/aceites.html')

def apis(request):
    return render(request,'core/api.html')

def marcas(request):
    return render(request,'core/marcas.html')

def verservicio(request):
    return render(request,'core/services.html')

def consulta(request):
    return render(request,'core/consultas.html')

def resumenpago(request):
    return render(request,'core/detalle_pago.html')

@permission_required('core.view_empleado')
def listar_consultas(request):
    # Obtener el usuario logueado
    user = request.user

    try:
        # Intentar obtener el cliente asociado al usuario
        cliente = Cliente.objects.get(user=user)
        # Filtrar los servicios agendados por el cliente logueado
        consultas = Mecanico_servicio.objects.filter(cliente=cliente)
    except Cliente.DoesNotExist:
        # Si no hay cliente asociado, mostrar todos los servicios
        consultas = Mecanico_servicio.objects.all()

    aux = {
        'lista': consultas
    }

    return render(request, 'core/consultas.html', aux)

#EMPLEADOS
@permission_required('core.view_empleado')
def empleados(request):
    empleados = Empleado.objects.all()
    aux = {
        'lista' : empleados
    }
    return render(request,'core/empleados/index.html', aux)

@permission_required('core.add_empleado')
def empleadosadd(request):
    aux ={
        'form' : EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Empleado Almacenado Correctamente!")
        else:
            aux['form'] = formulario
            #aux['msj'] = 'no se pudo almacenar!'
            messages.error(request, "no se pudo almacenar!")

    return render(request,'core/empleados/crud/add.html',aux)

@permission_required('core.change_empleado')
def empleadosupdate(request, id):
    empleado = Empleado.objects.get(id=id)
    aux ={
        'form' : EmpleadoForm(instance=empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST,instance=empleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Empleado Actualizado Correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request,"no se pudo Actualizar!")

            
    return render(request,'core/empleados/crud/update.html',aux)

@permission_required('core.delete_empleado')
def empleadosdelete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="empleados")

#TIPO EMPLEADO
@permission_required('core.view_tipo_empleado')
def tipoempleados(request):
    tipoempleados = TipoEmpleado.objects.all()
    aux = {
        'lista' : tipoempleados
    }
    return render(request,'core/tipoempleados/index.html', aux)

@permission_required('core.add_tipo_empleado')
def tipoempleadosadd(request):
    aux ={
        'form' : TipoEmpleadoForm()
    }

    if request.method == 'POST':
        formulario = TipoEmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Tipo empleado Almacenado Correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request,"no se pudo Almacenar!")

    return render(request,'core/tipoempleados/crud/add.html',aux)

@permission_required('core.change_tipo_empleado')
def tipoempleadosupdate(request, id):
    tipoempleado = TipoEmpleado.objects.get(id=id)
    aux ={
        'form' : TipoEmpleadoForm(instance=tipoempleado)
    }

    if request.method == 'POST':
        formulario = TipoEmpleadoForm(data=request.POST,instance=tipoempleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Tipo empleado Actualizado Correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request,"No se pudo Actualizar!")

            
    return render(request,'core/tipoempleados/crud/update.html',aux)

@permission_required('core.delete_tipo_empleado')
def tipoempleadosdelete(request, id):
    tipoempleado = TipoEmpleado.objects.get(id=id)
    tipoempleado.delete()

    return redirect(to="tipoempleados")

#Servicios
@permission_required('core.view_servicio')
def servicios(request):
    servicios = Servicio.objects.all()
    aux = {
        'lista' : servicios
    }
    return render(request,'core/servicios/index.html', aux)

@permission_required('core.add_servicio')
def serviciosadd(request):
    aux ={
        'form' : ServicioForm()
    }

    if request.method == 'POST':
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Servicio Almacenado Correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request,"No se pudo Almacenar!")

    return render(request,'core/servicios/crud/add.html',aux)

@permission_required('core.change_servicio')
def serviciosupdate(request, id):
    servicios = Servicio.objects.get(id=id)
    aux ={
        'form' : ServicioForm(instance=servicios)
    }

    if request.method == 'POST':
        formulario = TipoEmpleadoForm(data=request.POST,instance=servicios)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Servicio Actualizado Correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request,"No se pudo Actualizar!")

            
    return render(request,'core/servicios/crud/update.html',aux)

@permission_required('core.delete_servicio')
def serviciosdelete(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()

    return redirect(to="servicios")

'''
def servicios(request):
    servicio = Servicio.objects.all()
    aux = {
        'lista_serv' : servicio
    }
    return render(request,'core/services.html',aux)

def mecanicos(request):
    # Obtener el tipo de empleado que es mecánico
    tipo_mecanico = TipoEmpleado.objects.get(nombre='mecanico')
    mecanico = Empleado.objects.filter(tipo=tipo_mecanico)
    aux = {
        'lista_mecanico' : mecanico
    }
    return render(request, 'core/services.html',  aux)
'''

def salir(request):
    logout(request)

    return redirect(to="index")

def register(request):
    aux = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            grupo = Group.objects.get(name='cliente')
            user.groups.add(grupo)

            #MENSAJE
            messages.success(request, "Usuario creado correctamente!")
            # Crear una instancia del modelo Cliente
            Cliente.objects.create(
                user=user,
                rut_cliente=formulario.cleaned_data['rut_cliente'],
                nombre=formulario.cleaned_data['nombre'],
                apellido=formulario.cleaned_data['apellido'],
                direccion=formulario.cleaned_data['direccion'],
                celular=formulario.cleaned_data['celular'],
                edad=formulario.cleaned_data['edad'],
                patente=formulario.cleaned_data['patente']
            )

            # Autenticar y loguear al usuario
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            if user is not None:
                login(request, user)

            # Redirigir a la página de inicio
            return redirect('index')
        else:
            aux['form'] = formulario

    return render(request, 'registration/register.html', aux)

@login_required
def servicios_y_mecanicos(request):
    servicios = Servicio.objects.all()
    tipo_mecanico = TipoEmpleado.objects.get(descripcion='mecanico')
    mecanicos = Empleado.objects.filter(tipo=tipo_mecanico)

    rut_cliente = None
    if request.user.is_authenticated:
        try:
            cliente = Cliente.objects.get(user=request.user)
            rut_cliente = cliente.rut_cliente
        except Cliente.DoesNotExist:
            pass

    if request.method == 'POST':
        rut_cliente = request.POST.get('rut_cliente')
        patente_vehiculo = request.POST.get('patente_vehiculo')
        servicio_id = request.POST.get('servicio')
        mecanico_id = request.POST.get('mecanico')
        comentarios = request.POST.get('comentarios')

        # Almacena los datos del formulario en la sesión
        request.session['rut_cliente'] = rut_cliente
        request.session['patente_vehiculo'] = patente_vehiculo
        request.session['servicio_id'] = servicio_id
        request.session['mecanico_id'] = mecanico_id
        request.session['comentarios'] = comentarios

        return redirect('resumenpago')

    aux = {
        'lista_serv': servicios,
        'lista_mecanico': mecanicos,
        'rut_cliente': rut_cliente,
    }
    return render(request, 'core/booking.html', aux)

@login_required
def resumen_pedido(request):
    rut_cliente = request.session.get('rut_cliente')
    patente_vehiculo = request.session.get('patente_vehiculo')
    servicio_id = request.session.get('servicio_id')
    mecanico_id = request.session.get('mecanico_id')
    comentarios = request.session.get('comentarios')

    if not (rut_cliente and patente_vehiculo and servicio_id and mecanico_id):
        return redirect('core/booking.html')

    cliente = Cliente.objects.get(rut_cliente=rut_cliente)
    servicio = Servicio.objects.get(id=servicio_id)
    mecanico = Empleado.objects.get(rut=mecanico_id)

    # Obtener el valor del dólar
    response = requests.get('https://mindicador.cl/api/dolar/')
    if response.status_code == 200:
        data = response.json()
        valor_dolar = data.get('serie', [])[0].get('valor', 'No disponible') if data.get('serie') else 'No disponible'
        precio_float = float(servicio.precio)
        valor_total = round(precio_float / valor_dolar, 2)
    else:
        valor_dolar = 'No disponible'
    
    
    aux = {
        'cliente': cliente,
        'servicio': servicio,
        'mecanico': mecanico,
        'patente_vehiculo': patente_vehiculo,
        'comentarios': comentarios,
        'valor_dolar': valor_dolar,
        'valor_total': '{:.2f}'.format(valor_total)
    }
    return render(request, 'core/detalle_pago.html', aux)


def confirmar_pago(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        if data['status'] == 'COMPLETED':
            rut_cliente = request.session.get('rut_cliente')
            patente_vehiculo = request.session.get('patente_vehiculo')
            servicio_id = request.session.get('servicio_id')
            mecanico_id = request.session.get('mecanico_id')
            comentarios = request.session.get('comentarios')

            try:
                cliente = Cliente.objects.get(rut_cliente=rut_cliente)
                servicio = Servicio.objects.get(id=servicio_id)
                mecanico = Empleado.objects.get(rut=mecanico_id)

                Mecanico_servicio.objects.create(
                    servicio=servicio,
                    cliente=cliente,
                    mecanico=mecanico,
                    patente_vehiculo=patente_vehiculo,
                    comentarios=comentarios
                )

                # Limpia la sesión después de completar la transacción
                request.session.pop('rut_cliente')
                request.session.pop('patente_vehiculo')
                request.session.pop('servicio_id')
                request.session.pop('mecanico_id')
                request.session.pop('comentarios')

                # Redirige al usuario a la tabla de servicios
                return redirect(reverse('consulta'))

            except (Cliente.DoesNotExist, Servicio.DoesNotExist, Empleado.DoesNotExist) as e:
                # Manejar excepciones si el cliente, servicio o mecanico no existen
                return HttpResponseBadRequest('Algo salió mal durante la creación del servicio.')

        # Manejar otros estados de pago si es necesario
        # Ejemplo: 'PENDING', 'PROCESSING', etc.

    # Redirigir si no es una solicitud POST o si el estado del pago no es 'COMPLETED'
    return redirect('core/booking.html')
