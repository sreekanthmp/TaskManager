from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='tasks')

    def __str__(self):
        return self.title
