from django import forms
from .models import Category
class categoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Category name',
                'style': 'background-color: antiquewhite;'
            })
        }
    