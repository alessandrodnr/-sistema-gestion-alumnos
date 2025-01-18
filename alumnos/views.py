from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Alumno
from .forms import AlumnoForm
from django.db.models import Q  

def home(request):
    return render(request, 'alumnos/home.html')

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/listar.html', {'alumnos': alumnos})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumno agregado correctamente.')
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/agregar.html', {'form': form})

def modificar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumno modificado correctamente.')
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/modificar.html', {'form': form})

def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        messages.success(request, 'Alumno eliminado correctamente.')
        return redirect('listar_alumnos')
    return render(request, 'alumnos/eliminar.html', {'alumno': alumno})

def buscar_alumno(request):
    query = request.GET.get('q')
    if query:
        alumnos = Alumno.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellido_paterno__icontains=query) |
            Q(apellido_materno__icontains=query)
        )
        if not alumnos:
            messages.warning(request, 'No se encontraron resultados para la búsqueda.')
    else:
        alumnos = []
    return render(request, 'alumnos/buscar.html', {'alumnos': alumnos, 'query': query})
