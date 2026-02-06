from django.contrib import admin
from .models import DiseaseInfo, UserPrediction

# Register your models here.
admin.site.register(DiseaseInfo)
admin.site.register(UserPrediction)
