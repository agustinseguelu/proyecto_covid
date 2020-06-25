from django.shortcuts import render, HttpResponse, redirect
from .models import registros


def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == "POST":
        covidd = request.POST.get('covid','')
        habituales = request.POST.get('habituales', '')
        menos = request.POST.get('menos', '')
        graves = request.POST.get('graves', '')
        fecha = request.POST.get('fecha', '')

        if (menos== '' or graves=='' or habituales==''):
            return redirect('index')
        else:
            nuevo_registro = registros()
            nuevo_registro.dia = fecha
            nuevo_registro.covid = covidd
            nuevo_registro.sintomas = habituales
            nuevo_registro.sintomas = menos
            nuevo_registro.sintomas = graves
            nuevo_registro.save()
            return redirect('index')



        return redirect('index')

    sintomass = {'habituales': ['Fiebre', 'Tos seca', 'Cansancio', 'Ninguno'],
                  'menos' : ['Molestias y Dolores', 'Dolor de Garganta', 'Diarrea', 'Conjuntivitis', 'Dolores de cabeza', 'Pérdida del olfato o del gusto', 'Erupciones cutáneas o pérdida del color en extremidades', 'Insuficiencia Respiratorias', 'Ninguno'],
                  'graves' : ['Dificultad para respirar o sensación de falta de aire', 'Dolor o presión en el pecho', 'Incapacidad para hablar o moverse', 'Ninguno']}
    return render(request, 'registro.html', sintomass)

def estadistica(request):
    return render(request, 'estadistica.html')