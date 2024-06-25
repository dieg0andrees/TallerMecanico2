from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField

class EmpleadoForm(ModelForm):
    #captcha = CaptchaField()

    captcha = ReCaptchaField()
    
    class Meta:
        model = Empleado
        #fields = ['rut','nombre','apellido']
        fields = '__all__'

class TipoEmpleadoForm(ModelForm):

    class Meta:
        model = TipoEmpleado
        fields = '__all__'

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'   

class CustomUserCreationForm(UserCreationForm):
    rut_cliente = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=60)
    celular = forms.CharField(max_length=15)
    edad = forms.IntegerField()
    patente = forms.CharField(max_length=10)
    
    class Meta:
        model = User
        fields = ['username','nombre', 'apellido', 'rut_cliente', 'email','direccion', 'celular', 'edad', 'patente', 'password1', 'password2']