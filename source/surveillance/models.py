from django.db import models


class Village(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class HealthReport(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    diarrhea_cases = models.IntegerField(default=0)
    vomiting_cases = models.IntegerField(default=0)
    water_ph = models.FloatField(default=7.0)
    water_turbidity = models.FloatField(default=1.0)
    risk_score_output = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
