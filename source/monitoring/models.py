from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from .risk_engine import RiskEngine


class UserProfile(models.Model):
    ROLES = [
        ('Field Officer', 'Field Officer'),
        ('District Admin', 'District Admin'),
        ('State Admin', 'State Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLES, default='Field Officer')
    district = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class WaterSample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    village = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_collected = models.DateField(default=timezone.now)

    # Basic Water Parameters
    turbidity = models.FloatField(help_text="Turbidity in NTU")
    ph = models.FloatField(help_text="pH value")
    ecoli_present = models.BooleanField(default=False, help_text="Presence of E.coli")
    nitrate_level = models.FloatField(help_text="Nitrate level in mg/L")

    # Advanced Chemical Parameters
    dissolved_oxygen = models.FloatField(default=0.0, help_text="DO in mg/L")
    bod = models.FloatField(default=0.0, help_text="BOD in mg/L")
    cod = models.FloatField(default=0.0, help_text="COD in mg/L")
    nitrite_level = models.FloatField(default=0.0, help_text="Nitrite level in mg/L")
    ammonia = models.FloatField(default=0.0, help_text="Ammonia in mg/L")
    fluoride = models.FloatField(default=0.0, help_text="Fluoride in mg/L")
    chloride = models.FloatField(default=0.0, help_text="Chloride in mg/L")
    sulphate = models.FloatField(default=0.0, help_text="Sulphate in mg/L")

    # Heavy Metals
    lead = models.FloatField(default=0.0, help_text="Lead in mg/L")
    arsenic = models.FloatField(default=0.0, help_text="Arsenic in mg/L")
    mercury = models.FloatField(default=0.0, help_text="Mercury in mg/L")
    cadmium = models.FloatField(default=0.0, help_text="Cadmium in mg/L")
    iron = models.FloatField(default=0.0, help_text="Iron in mg/L")
    water_source = models.CharField(max_length=100, choices=[
        ('Borewell', 'Borewell'),
        ('River', 'River'),
        ('Lake', 'Lake'),
        ('Panchayat Supply', 'Panchayat Supply'),
        ('Tapwater', 'Tapwater'),
        ('Other', 'Other')
    ])

    # Submitter Contact
    phone_number = models.CharField(max_length=20, blank=True, null=True, help_text="WhatsApp Number for Alerts")

    # Calculated Fields
    contamination_index = models.FloatField(blank=True, null=True)
    risk_score = models.FloatField(blank=True, null=True)
    cause = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    remedy = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        engine = RiskEngine()
        
        # All 18 parameters
        params = [
            self.turbidity, self.ph, self.ecoli_present, self.nitrate_level,
            self.dissolved_oxygen, self.bod, self.cod, self.nitrite_level,
            self.ammonia, self.fluoride, self.chloride, self.sulphate,
            self.lead, self.arsenic, self.mercury, self.cadmium, self.iron
        ]
        ci = engine.calculate_contamination_index(self.village, *params)
        prediction = engine.predict_risk(self.village, *params)
        self.contamination_index = ci
        self.risk_score = prediction[1]  # Probability from ML model

        # Generate Insights
        self.cause, self.effect, self.remedy = engine.generate_insights(self.village, *params)

        super().save(*args, **kwargs)

        # Trigger Alert if High Risk
        alert_level = engine.determine_alert_level(self.risk_score)
        if self.risk_score > 70:
            Alert.objects.create(
                sample=self,
                village=self.village,
                district=self.district,
                risk_score=self.risk_score,
                alert_level=alert_level
            )

    def __str__(self):
        return f"{self.village} - {self.date_collected}"


class Alert(models.Model):
    ALERT_LEVELS = [
        ('Green', 'Low Risk'),
        ('Yellow', 'Moderate Risk'),
        ('Red', 'High Risk')
    ]

    sample = models.OneToOneField(WaterSample, on_delete=models.CASCADE)
    village = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    risk_score = models.FloatField()
    alert_level = models.CharField(max_length=20, choices=ALERT_LEVELS)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                    blank=True, related_name='resolved_alerts')
    resolution_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.alert_level} Alert - {self.village}"


# --- HACKATHON PIVOT: ACTIVE PREDICTIVE LOGISTICS ENGINE ---

class VillageProfile(models.Model):
    """Stores persistent data for communities to calculate Triage Scores and track health."""
    name = models.CharField(max_length=100, unique=True, help_text="Village Name")
    district = models.CharField(max_length=100)
    population = models.IntegerField(default=5000, help_text="Estimated Population")
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} ({self.population} pop)"


class PHCHealthReport(models.Model):
    """Primary Health Centre (PHC) Community Data Sync. Acts as a human sensor."""
    village = models.ForeignKey(VillageProfile, on_delete=models.CASCADE, related_name='health_reports')
    date_reported = models.DateField(default=timezone.now)
    gastro_cases = models.IntegerField(default=0, help_text="Sudden spike in diarrhea/vomiting")
    fever_cases = models.IntegerField(default=0)
    notes = models.TextField(blank=True, help_text="Officer notes on outbreak severity")

    def __str__(self):
        return f"{self.village.name} Report - {self.gastro_cases} Gastro Cases"
