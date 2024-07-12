from django.forms import ModelForm
from tasks.models import Task
from projects.models import Project
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
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        if user:
            projects = Project.objects.filter(owner=user).order_by("id")
            unassigned_project = projects.filter(name="Unassigned").first()
            if unassigned_project:
                projects = projects.exclude(id=unassigned_project.id)
            choices = [(project.id, project.name) for project in projects]
            if unassigned_project:
                choices.append((unassigned_project.id, unassigned_project.name))
            self.fields["project"].choices = choices
            if unassigned_project:
                self.fields["project"].initial = unassigned_project.id
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
            "is_completed": forms.CheckboxInput(attrs={"class": "checkbox", "style": "color: red;"})
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(EditTaskForm, self).__init__(*args, **kwargs)
        if user:
            projects = Project.objects.filter(owner=user).order_by('id')
            unassigned_project = projects.filter(name="Unassigned").first()
            if unassigned_project:
                projects = projects.exclude(id=unassigned_project.id)
            choices = [(project.id, project.name) for project in projects]
            if unassigned_project:
                choices.append((unassigned_project.id, unassigned_project.name))
                if len(choices) == 2:
                    self.fields["project"].initial = unassigned_project.id
            self.fields["project"].choices = choices
