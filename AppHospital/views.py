from django.shortcuts import render
from django.http import HttpResponse

from AppHospital.models import *
from AppHospital.forms import *

# Create your views here.

def inicioTemplate(request):

    return render(request, "AppHospital/inicio.html")

def pacienteTemplate(request):

        if request.method == "POST":

            formulario = PacienteFormulario(request.POST)

            if formulario.is_valid():

                datos = formulario.cleaned_data

                try:
                    paciente = Paciente(nombre = datos['nombre'], apellido = datos['apellido'], dni = datos['dni'], obra_social = datos['obra_social'], nro_afiliado = datos['nro_afiliado'])

                    paciente.save()
                    mensaje = "El paciente se guardó correctamente"
                    formulario = PacienteFormulario()
                    return render(request, "AppHospital/alta_pacientes.html", {"formulario": formulario, "Mensaje": mensaje})

                except:
                    mensaje = "El paciente ya existe"
                    return render(request, "AppHospital/alta_pacientes.html", {"formulario": formulario, "Mensaje": mensaje})
        else:

            formulario = PacienteFormulario()

            return render(request, "AppHospital/alta_pacientes.html", {"formulario": formulario})

        return render(request, "AppHospital/alta_pacientes.html", {"formulario": formulario})

def pacienteBusqueda(request):

    return render(request, "AppHospital/consulta_pacientes.html")

def pacienteResultado(request):

    if request.GET["dni"]:

        try:

            dni = request.GET.get('dni', "")
            paciente = Paciente.objects.get(dni = dni)
            
            return render(request, "AppHospital/resultado_pacientes.html", {"paciente":paciente})

        except:

            mensaje = "El paciente no existe en la base de datos"

            return render(request, "AppHospital/consulta_pacientes.html", {"Mensaje":mensaje})

    else:

        mensaje = "No enviaste datos"

        return render(request, "AppHospital/consulta_pacientes.html", {"Mensaje":mensaje})

def medicoTemplate(request):

        if request.method == "POST":

            formulario = MedicoFormulario(request.POST)

            if formulario.is_valid():

                datos = formulario.cleaned_data

                try:
                    medico = Medico(nombre = datos['nombre'], apellido = datos['apellido'], especialidad = datos['especialidad'], dni = datos['dni'])

                    medico.save()
                    mensaje = "El médico se guardó correctamente"
                    formulario = MedicoFormulario()
                    return render(request, "AppHospital/alta_medicos.html", {"formulario": formulario, "Mensaje": mensaje})

                except:
                    mensaje = "El médico ya existe"
                    return render(request, "AppHospital/alta_medicos.html", {"formulario": formulario, "Mensaje": mensaje})
        else:

            formulario = MedicoFormulario()

            return render(request, "AppHospital/alta_medicos.html", {"formulario": formulario})

        return render(request, "AppHospital/alta_medicos.html", {"formulario": formulario})

def turnoTemplate(request):

        if request.method == "POST":

            formulario = TurnoFormulario(request.POST)

            if formulario.is_valid():

                datos = formulario.cleaned_data

                try:
                    turno = Turno(fecha = datos['fecha'], hora = datos['hora'], paciente = datos['paciente'], medico = datos['medico'])

                    turno.save()
                    mensaje = "El Turno se guardó correctamente"
                    formulario = TurnoFormulario()
                    return render(request, "AppHospital/alta_turnos.html", {"formulario": formulario, "Mensaje": mensaje})

                except:
                    
                    return render(request, "AppHospital/alta_turnos.html", {"formulario": formulario, "Mensaje": mensaje})
        else:

            formulario = TurnoFormulario()

            return render(request, "AppHospital/alta_turnos.html", {"formulario": formulario})

        return render(request, "AppHospital/alta_turnos.html", {"formulario": formulario})