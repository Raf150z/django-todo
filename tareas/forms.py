from django import forms
from .models import Tareas

class TareasForm(forms.ModelForm):
    
    class Meta:
        model = Tareas
        
        fields = '__all__'