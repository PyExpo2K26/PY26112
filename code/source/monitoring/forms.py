from django import forms
from .models import WaterSample


class WaterSampleForm(forms.ModelForm):
    class Meta:
        model = WaterSample
        fields = [
            'village', 'district', 'latitude', 'longitude', 'date_collected',
            'water_source', 'turbidity', 'ph', 'nitrate_level', 'ecoli_present',
            'dissolved_oxygen', 'bod', 'cod', 'nitrite_level', 'ammonia',
            'fluoride', 'chloride', 'sulphate',
            'lead', 'arsenic', 'mercury', 'cadmium', 'iron',
            'phone_number'
        ]
        widgets = {
            'date_collected': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'village': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'water_source': forms.Select(attrs={'class': 'form-select'}),
            'turbidity': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'ph': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'nitrate_level': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'ecoli_present': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            
            # New Advanced Fields
            'dissolved_oxygen': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'bod': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'cod': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'nitrite_level': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'ammonia': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'fluoride': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'chloride': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'sulphate': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            
            # New Heavy Metals
            'lead': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'arsenic': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'mercury': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'cadmium': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'iron': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        }
