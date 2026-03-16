from django import forms
from .models import WaterSample


class WaterSampleForm(forms.ModelForm):
    class Meta:
        model = WaterSample
        fields = [
            'village', 'district', 'latitude', 'longitude', 'date_collected',
            'water_source', 'turbidity', 'ph', 'nitrate_level', 'ecoli_present',
            'phone_number'
        ]
        widgets = {
            'date_collected': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'village': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'water_source': forms.Select(attrs={'class': 'form-select'}),
            'turbidity': forms.NumberInput(attrs={'class': 'form-control'}),
            'ph': forms.NumberInput(attrs={'class': 'form-control'}),
            'nitrate_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'ecoli_present': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +91 9876543210'})
        }
