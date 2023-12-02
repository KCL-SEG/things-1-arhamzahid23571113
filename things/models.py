from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=100)  # Short string for name
    description = models.TextField()          # Longer string for description
    quantity = models.IntegerField()          # Integer for quantity

