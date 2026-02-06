from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiseaseInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    remedy = models.TextField()
    bio_profile = models.TextField(help_text="JSON-like string of biochemical values")
    
    def __str__(self):
        return self.name

class UserPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predictions')
    symptom_text = models.TextField()
    water_color = models.CharField(max_length=50)
    water_odor = models.CharField(max_length=50)
    prediction = models.CharField(max_length=100)
    remedy = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.prediction} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
