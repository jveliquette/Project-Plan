from django.db import models
from projects.models import Project
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assigned_to = models.ForeignKey(
        User,
        related_name="tasks",
        on_delete=models.CASCADE,
        default=1
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
