# alumnos/forms.py
from django import forms
from .models import Alumno
from django.core.exceptions import ValidationError

class AlumnoForm(forms.ModelForm):
    fecha_ingreso = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Alumno
        fields = '__all__'

    def clean_promedio_em(self):
        promedio = self.cleaned_data['promedio_em']
        if promedio < 1.0 or promedio > 7.0:
            raise ValidationError('El promedio debe estar entre 1.0 y 7.0')
        return promedio