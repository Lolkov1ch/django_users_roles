from django.db import models
from django.contrib.auth.models import User  

class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В процесі'),
        ('completed', 'Виконано'),
        ('deferred', 'Відкладено'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})" # type: ignore
