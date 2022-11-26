from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Member(models.Model):
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='member'
    )

class Team(models.Model):
    leader = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="leader"
    )
    team_member = models.ManyToManyField("Member")
