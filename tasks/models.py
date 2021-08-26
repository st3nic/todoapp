from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices

class Task(models.Model):

    Priorities = (
        ('High', 'HIGH'),
        ('Medium', 'MEDIUM'),
        ('Low', 'LOW'),
    )

    Status = (
        ('New', 'NEW'),
        ('In Progress', 'IN PROGRESS'),
        ('Complete', 'COMPLETE'),
    )

    task = models.CharField(max_length=50)
    priority = models.CharField(max_length=50, choices=Priorities)
    status = models.CharField(max_length=50, choices=Status, default='New')
    who = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task

