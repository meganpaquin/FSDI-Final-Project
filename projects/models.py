from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField()
    deadline = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="project_author"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="project_assignee"
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )

    # need to add tasks
    # need to add milestones

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', args=[self.id])
