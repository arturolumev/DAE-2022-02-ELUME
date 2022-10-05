from django.forms import ModelForm
from .models import *

class AlumnoForm(ModelForm):
    class Meta:
        model = TblAlumno
        fields = '__all__' #Ingresa como usuario "admin" y como contraseña "Tecsup2019"
