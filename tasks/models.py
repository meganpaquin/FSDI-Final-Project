from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name

        
class Task(models.Model):
    task_name = models.CharField(max_length=120)
    task_summary = models.TextField()
    task_details = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="task_assignee"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="task_author"
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    
    # need to add status
    # need to add risks / issues
    # need to add Project

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail', args=[self.id])

