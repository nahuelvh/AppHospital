from django.contrib import admin
from django.urls import path
from AppHospital.views import *

urlpatterns = [
    path('', inicioTemplate),
    path('turnos/', turnoTemplate, name = "Turnos"),

]
