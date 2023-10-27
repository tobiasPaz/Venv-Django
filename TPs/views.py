from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import JsonResponse

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

def crear_proyectos(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        # return JsonResponse({'nombre': nombre, 'descripcion': descripcion})
        Proyecto.objects.create(nombre=nombre, descripcion=descripcion)
        return HttpResponseRedirect('/TPs')
    context = {'safe': True}
    return render(request, 'crear_proyectos.html', context)

def borrar_proyecto(request, proyecto_id):
    if request.method == 'DELETE':
        proyecto = Proyecto.objects.get(id=proyecto_id)
        proyecto.delete()
        return JsonResponse({'success': True}) 

def crear_item(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    if request.method == 'POST':
        nombre_item = request.POST['nombre-item']
        descripcion_item = request.POST['descripcion-item']
        Item.objects.create(proyecto=proyecto, nombre=nombre_item, descripcion=descripcion_item)
        return HttpResponseRedirect(f'/TPs/{proyecto_id}')