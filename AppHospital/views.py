from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicioTemplate(request):

    return render(request, "AppHospital/index.html")

def turnoTemplate(request):

    return HttpResponse("Pagina Turnos")