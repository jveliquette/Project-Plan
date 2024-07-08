from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

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
    assignee = models.ForeignKey(
        User,
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True,
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class TaskChart(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    week_number = models.CharField(max_length=2, blank=True)
    project = models.ForeignKey(
        Project,
        related_name="task_chart",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
            User,
            related_name="task_chart",
            on_delete=models.CASCADE,
            null=True,
        )

    def __str__(self):
        return self.name

    # Overiding save method
    def save(self, *args, **kwargs):
        if self.week_number == "":
            self.week_number = str(self.start_date.isocalendar()[1])
        super().save(*args, **kwargs)
