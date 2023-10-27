from django.urls import path
from . import views

urlpatterns = [
    path('', views.TPs),
    path("<int:proyecto_id>", views.TPsDetalles),
    path('crear_proyectos', views.crear_proyectos),
    path('crear_item/<int:proyecto_id>', views.crear_item),
    path('borrar_proyecto/<int:proyecto_id>', views.borrar_proyecto),
]