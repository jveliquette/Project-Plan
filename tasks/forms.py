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
            "assignee",
        ]
        widgets = {
            "start_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

class TaskNotesForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "notes",
        ]
