from .models import Students
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'address', 'password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput( render_value=True,attrs={'class': 'form-control'}),
        }
        ordering = ['-id']