from django.urls import path
from . import views

urlpatterns = [
path('',views.lista_tareas,name='lista'),
path('crear/',views.crear_tareas,name='crear'),
path('editar/<int:id>/', views.editar_tarea,name='editar'),
path('eliminar/<int:id>/',views.eliminar_tarea,name='eliminar'),
path('completar/<int:id>/',views.completar_tarea,name='completar'),
]