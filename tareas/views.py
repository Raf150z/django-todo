from django.shortcuts import render,redirect,get_object_or_404
from .models import Tareas
from .forms import TareasForm

def lista_tareas(request):
    
    tareas = Tareas.objects.all().order_by('-fecha_creacion')
    
    return render(
        request,
        'tareas/lista.html',
        {'tareas': tareas}
    )
    
    
def crear_tareas(request):
    
    form = TareasForm(request.POST or None)
    
    if form.is_valid():
        
        form.save()
        
        return redirect('lista')
    
    return render(
        request,
        'tareas/form.html',
        {'form': form}
    )
    
    
def editar_tarea(request,id):
    
    tareas = get_object_or_404(
        Tareas,
        id=id
    )
    
    form = TareasForm(
        request.POST or None,
        instance=tareas
    )
    
    if form.is_valid():
        
        form.save()
        
        return redirect('lista')
    
    return render(
        request,
        'tareas/form.html',
        {'form': form}
    )
    
    
def eliminar_tarea(request,id):
    
    tareas = get_object_or_404(
        Tareas,
        id=id
    )
    
    tareas.delete()
    
    return redirect('lista')


def completar_tarea(request,id):
    
    tareas = get_object_or_404(
        Tareas,
        id=id
    )
    
    tareas.completada = True
    
    tareas.save()
    
    return redirect('lista')