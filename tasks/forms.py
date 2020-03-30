from django import forms
from tasks.models import Task, TaskStatus, Tag
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'assigned_to', 'tags')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'ArrayOfTaskStatus'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control',
                                                'size': 9, 'id': 'ArrayOfTaskTag'}),
        }


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ('name',)


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
