
from django.shortcuts import get_object_or_404, get_list_or_404,render
from django.http import HttpResponse, Http404
from .models import Killer

def mostrar_killers(request):
    inicio = get_list_or_404(Killer.objects.order_by('nombre'))
    return render(request, 'visualizar.html', {"killers":inicio})

def mostrar_killer(request,killer_id):
    killer = get_object_or_404(Killer,pk=killer_id)
    return render(request, 'zoom.html', {"killer" : killer})

def registro_killer(request):
    return render(request,"registro.html")

def index(request):
    return render(request,"index.html")