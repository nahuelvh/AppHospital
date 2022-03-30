from django.contrib import admin
from django.urls import path
from AppHospital.views import *

urlpatterns = [
 #   path('', inicioTemplate),
    path('alta_turnos/', turnoTemplate, name = "AltaTurnos"),
    path('alta_pacientes/', pacienteTemplate, name = "AltaPacientes"),
    path('alta_medicos/', medicoTemplate, name = "AltaMedicos"),
    path('consulta_pacientes/', pacienteBusqueda, name = "ConsultaPacientes"),
    path('resultado_pacientes/', pacienteResultado, name = "ResultadoPacientes"),

]
