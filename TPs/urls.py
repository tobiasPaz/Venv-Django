from django.urls import path
from . import views

urlpatterns = [
    path('', views.TPs),
    path("<int:proyecto_id>", views.TPsDetalles),
]