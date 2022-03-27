from django.contrib import admin
from django.urls import path
from AppHospital.views import *

urlpatterns = [
 #   path('', inicioTemplate),
    path('turnos/', turnoTemplate, name = "Turnos"),
    path('alta_pacientes/', pacienteTemplate, name = "AltaPacientes"),
    path('medicos/', medicoTemplate, name = "Medicos"),
    path('consulta_pacientes/', pacienteBusqueda, name = "ConsultaPacientes"),
    path('resultado_pacientes/', pacienteResultado, name = "ResultadoPacientes")
]
