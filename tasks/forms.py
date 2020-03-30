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

    def clean(self):
        cleaned_data = super(StatusCreateForm, self).clean()
        if TaskStatus.objects.filter(name=self.cleaned_data.get('name')).exists():
            raise ValidationError('This status has already created')
        return cleaned_data


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

    def clean(self):
        cleaned_data = super(TagCreateForm, self).clean()
        if Tag.objects.filter(name=self.cleaned_data.get('name')).exists():
            raise ValidationError('This tag has already created')
        return cleaned_data
