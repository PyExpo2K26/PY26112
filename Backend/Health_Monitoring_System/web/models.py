from django.db import models

# Create your models here.
class DiseaseInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    remedy = models.TextField()
    bio_profile = models.TextField(help_text="JSON-like string of biochemical values")
    
    def __str__(self):
        return self.name
