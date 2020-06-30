from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .models import registros
from .forms import registrosForm



def registro(request):
    form = registrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        context= {'form': form }
        
        return render(request, 'registro.html', context)

      
    if request.POST:
        covidd = request.post.get('covid','')
        habituales = request.post.get('habituales', '')
        menos = request.post.get('menos', '')
        graves = request.post.get('graves', '')
        fecha = request.post.get('fecha', '')

        if (menos== '' or graves=='' or habituales==''):
            return redirect('registro.html')
        else:
            nuevo_registro = registros()
            nuevo_registro.dia = fecha
            nuevo_registro.covid = covidd
            nuevo_registro.sintomas = habituales
            nuevo_registro.sintomas = menos
            nuevo_registro.sintomas = graves
            nuevo_registro.save()
            return redirect('index.html')
    
    sintomass = {'habituales': ['Fiebre', 'Tos seca', 'Cansancio', 'Ninguno'],
                  'menos' : ['Molestias y Dolores', 'Dolor de Garganta', 'Diarrea', 'Conjuntivitis', 'Dolores de cabeza', 'Pérdida del olfato o del gusto', 'Erupciones cutáneas o pérdida del color en extremidades', 'Insuficiencia Respiratorias', 'Ninguno'],
                  'graves' : ['Dificultad para respirar o sensación de falta de aire', 'Dolor o presión en el pecho', 'Incapacidad para hablar o moverse', 'Ninguno']}
    return render(request, 'registro.html', sintomass)


def estadistica(request):
    return render(request, 'estadistica.html')


# Lo de Agustin

def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    return redirect('/login')


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "register.html", {'form': form})


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "login.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')