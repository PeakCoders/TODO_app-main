from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    title_task = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...', 'class':'form-control'}))
    
   
    class Meta:
        model = Task
        fields = '__all__'