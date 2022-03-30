from django import forms
from AppHospital.models import Medico, Paciente

class PacienteFormulario(forms.Form):

    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    obra_social = forms.CharField(max_length=60)
    nro_afiliado = forms.IntegerField()

class MedicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=60)
    dni = forms.IntegerField()

class TurnoFormulario(forms.Form):
    fecha = forms.DateField()
    hora = forms.CharField(max_length=5)
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.order_by('apellido', 'nombre'))
    medico = forms.ModelChoiceField(queryset=Medico.objects.order_by('apellido', 'nombre'))