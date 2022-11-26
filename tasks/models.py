from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from projects.models import Project


class Priority(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name

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
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )

    # need to add risks / issues

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('task-detail', args=[self.id])


class Risk(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
       get_user_model(),
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    comment = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment