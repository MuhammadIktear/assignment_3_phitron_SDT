# task/forms.py
from django import forms
from .models import Task
from category.models import Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter title here',
                'style': 'background-color: antiquewhite;'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter description here',
                'style': 'background-color: antiquewhite;'
            }),
            'assign_date': forms.DateInput(attrs={
                'placeholder': 'Select a date',
                'style': 'background-color: antiquewhite;',
                'type': 'date'
            }),
            'is_complete': forms.CheckboxInput(attrs={
                'style': 'background-color: antiquewhite;'
            }),
            'category': forms.CheckboxSelectMultiple(attrs={
                'style': 'background-color: antiquewhite;'
            }),
        }
