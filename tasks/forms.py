from django.forms import ModelForm
from tasks.models import Task
from django import forms


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"type": "input", "placeholder": "Enter task name..."}),
            "start_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "project": forms.Select(attrs={"class": "select"}),
        }

class TaskNotesForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "notes",
        ]
        widgets = {
            "notes": forms.Textarea(attrs={"class": "textarea", "placeholder": "Enter notes..."})
        }

class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "is_completed",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"type": "input", "placeholder": "Enter task name..."}),
            "start_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "project": forms.Select(attrs={"class": "select"}),
        }
