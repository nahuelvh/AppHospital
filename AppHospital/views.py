from django.shortcuts import render
from django.http import HttpResponse

from AppHospital.models import *

# Create your views here.

def inicioTemplate(request):

    return render(request, "AppHospital/inicio.html")

def turnoTemplate(request):

    return render(request, "AppHospital/turnos.html")

def medicoTemplate(request):

    return render(request, "AppHospital/medicos.html")

def pacienteTemplate(request):

    if request.method == "POST":
        
        try:

            paciente = Paciente( None, request.POST['nombre'], request.POST['apellido'], request.POST['DNI'], request.POST['obra_social'], request.POST['nro_afiliado'])
            paciente.save()

        except:
                  
            return render(request, "AppHospital/alta_pacientes.html")

        return render(request, "AppHospital/alta_pacientes.html")

    return render(request, "AppHospital/alta_pacientes.html")

def pacienteBusqueda(request):

    return render(request, "AppHospital/consulta_pacientes.html")

def pacienteResultado(request):

    if request.GET["dni"]:

        dni = request.GET.get('dni', "")
        paciente = Paciente.objects.get(dni = dni)
        print(paciente)
        return render(request, "AppHospital/resultado_pacientes.html", {"paciente" : paciente})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)