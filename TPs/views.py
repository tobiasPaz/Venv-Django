from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Proyecto, Item

def TPs(request):
    proyectos = Proyecto.objects.order_by('nombre')
    plantilla = loader.get_template('index.html')
    context = {"proyectos": proyectos}
    return HttpResponse(plantilla.render(context, request))

def TPsDetalles(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    item = Item.objects.filter(proyecto=proyecto)
    plantilla = loader.get_template('proyecto.html')
    context = {"proyecto": proyecto, "items": item}
    return HttpResponse(plantilla.render(context, request))