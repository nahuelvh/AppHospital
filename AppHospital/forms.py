from django import forms
from AppHospital.models import Medico, Paciente

class PacienteFormulario(forms.Form):

    nombre = forms.CharField(max_length=20, label = "Nombre")
    apellido = forms.CharField(max_length=30, label = "Apellido")
    dni = forms.IntegerField(label = "DNI")
    obra_social = forms.CharField(max_length=60, label = "Obra Social")
    nro_afiliado = forms.IntegerField(label = "Número de Afiliado")

class MedicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, label = "Nombre")
    apellido = forms.CharField(max_length=30, label = "Apellido")
    especialidad = forms.CharField(max_length=60, label = "Especialidad")
    matricula = forms.IntegerField(label = "Mátricula")

class TurnoFormulario(forms.Form):
    fecha = forms.DateField(label = "Fecha")
    hora = forms.CharField(max_length=5, label = "Hora")
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.order_by('apellido', 'nombre'), label = "Paciente")
    medico = forms.ModelChoiceField(queryset=Medico.objects.order_by('apellido', 'nombre'), label = "Médico")