from django import forms
from .models import User
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['product', 'price', 'quantity']
        widgets = {
            'product': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),

        }