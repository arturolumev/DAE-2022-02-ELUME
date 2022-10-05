from django.shortcuts import render, redirect
from django.views import View

from .forms import *
# importamos la libreria generic

from .models import TblAlumno

class IndexView(View):
    
    def get(self, request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos':listaAlumnos,
            'formAlumno': formAlumno
        }
        
        return render(request, 'index.html', context)
    
    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            # <process form cleaned data>
            return redirect('/')