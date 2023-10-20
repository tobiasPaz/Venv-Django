from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Proyecto, Item

def TPs(request):
    item = Item.objects.order_by('nombre')
    proyecto = Proyecto.objects.order_by('nombre')
    plantilla = loader.get_template('index.html')
    # return HttpResponse(plantilla.render())
    context = {"proyecto": proyecto, "item": item}
    return HttpResponse(plantilla.render(context, request))
