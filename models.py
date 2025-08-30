# backend/models.py
from django.db import models

class SafeZone(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    geometry = models.JSONField()  # GeoJSON polygon
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name


class Alert(models.Model):
    LEVEL_CHOICES = [
        ('safe', 'Safe'),
        ('warning', 'Warning'),
        ('danger', 'Danger'),
    ]
    title = models.CharField(max_length=150)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title