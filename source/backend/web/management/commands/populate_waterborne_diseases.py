"""
Management command to populate the database with waterborne diseases.
Usage: python manage.py populate_waterborne_diseases
"""

from django.core.management.base import BaseCommand
from web.models import DiseaseInfo
import json


class Command(BaseCommand):
    help = 'Populate database with waterborne disease information'

    def handle(self, *args, **options):
        diseases = [
            {
                "name": "Cholera",
                "remedy": "Rehydration is the most important treatment. Rapidly replace fluids and electrolytes lost through diarrhea using Oral Rehydration Salts (ORS). In severe cases, intravenous fluids are required. Antibiotics (like tetracycline or doxycycline) can shorten the duration of the illness. Prevention through proper water sanitation and vaccination is essential.",
                "bio_profile": {
                    "Sodium_mmol_L": 130.5,
                    "Potassium_mmol_L": 3.1,
                    "Chloride_mmol_L": 92.5,
                    "WBC_109_per_L": 13.5,
                    "Hemoglobin_g_dL": 13.8,
                    "Platelets_109_per_L": 210.0,
                    "Urea_mg_dL": 48.0,
                    "Creatinine_mg_dL": 1.5,
                    "Bilirubin_mg_dL": 0.9,
                    "ALT_U_L": 40.0,
                    "AST_U_L": 45.0
                }
            },
            {
                "name": "Typhoid",
                "remedy": "Typhoid fever is treated with antibiotics such as ciprofloxacin, ceftriaxone, or azithromycin depending on resistance patterns. It is essential to complete the full course of antibiotics (7-14 days). Supportive care includes fluid replacement, nutritional support with a soft diet, and monitoring for complications. Management of fever with acetaminophen (not NSAIDs). Prevention via vaccination (Typhi conjugate vaccine or oral Ty21a vaccine) is highly recommended before traveling to endemic areas.",
                "bio_profile": {
                    "Sodium_mmol_L": 135.5,
                    "Potassium_mmol_L": 3.9,
                    "Chloride_mmol_L": 99.5,
                    "WBC_109_per_L": 3.8,
                    "Hemoglobin_g_dL": 11.4,
                    "Platelets_109_per_L": 143.0,
                    "Urea_mg_dL": 31.0,
                    "Creatinine_mg_dL": 0.9,
                    "Bilirubin_mg_dL": 1.5,
                    "ALT_U_L": 88.0,
                    "AST_U_L": 76.0
                }
            },
            {
                "name": "Hepatitis A",
                "remedy": "There is no specific antiviral treatment for Hepatitis A. Management is entirely supportive: adequate rest in the acute phase, proper nutrition with small frequent meals, adequate hydration, and monitoring of liver function. Avoid alcohol and hepatotoxic medications (like acetaminophen) until full recovery. Most patients recover completely within 2-12 weeks. Vaccination with inactivated Hepatitis A vaccine is available and highly effective for prevention.",
                "bio_profile": {
                    "Sodium_mmol_L": 139.0,
                    "Potassium_mmol_L": 4.2,
                    "Chloride_mmol_L": 102.5,
                    "WBC_109_per_L": 7.0,
                    "Hemoglobin_g_dL": 13.2,
                    "Platelets_109_per_L": 178.0,
                    "Urea_mg_dL": 25.0,
                    "Creatinine_mg_dL": 0.8,
                    "Bilirubin_mg_dL": 4.5,
                    "ALT_U_L": 847.0,
                    "AST_U_L": 725.0
                }
            },
            {
                "name": "Dysentery",
                "remedy": "Treatment focuses on replacing lost fluids and electrolytes with ORS. For bacterial dysentery (Shigellosis), antibiotics like ciprofloxacin, azithromycin, or ceftriaxone are used based on resistance patterns. For amoebic dysentery, amoebicidal drugs like metronidazole or iodoquinol are first-line treatments. Avoid anti-diarrheal medications (loperamide) which can worsen the condition and increase complications. Severe cases may require hospitalization for parenteral fluid and electrolyte replacement.",
                "bio_profile": {
                    "Sodium_mmol_L": 136.0,
                    "Potassium_mmol_L": 3.5,
                    "Chloride_mmol_L": 98.0,
                    "WBC_109_per_L": 14.2,
                    "Hemoglobin_g_dL": 12.8,
                    "Platelets_109_per_L": 250.0,
                    "Urea_mg_dL": 35.0,
                    "Creatinine_mg_dL": 1.1,
                    "Bilirubin_mg_dL": 0.7,
                    "ALT_U_L": 30.0,
                    "AST_U_L": 32.0
                }
            },
            {
                "name": "Giardiasis",
                "remedy": "Metronidazole (250 mg three times daily for 5-7 days), tinidazole (single 2g dose), or nitazoxanide are the preferred medications for treating giardiasis. Ensure adequate hydration throughout treatment. Dietary management includes avoiding lactose-containing foods during acute phase as lactose intolerance may develop post-infection. Strict hand hygiene and safe water practices are essential to prevent spread within households.",
                "bio_profile": {
                    "Sodium_mmol_L": 140.5,
                    "Potassium_mmol_L": 4.3,
                    "Chloride_mmol_L": 104.0,
                    "WBC_109_per_L": 7.6,
                    "Hemoglobin_g_dL": 13.1,
                    "Platelets_109_per_L": 219.0,
                    "Urea_mg_dL": 28.0,
                    "Creatinine_mg_dL": 0.9,
                    "Bilirubin_mg_dL": 0.6,
                    "ALT_U_L": 24.0,
                    "AST_U_L": 22.0
                }
            },
            {
                "name": "E. coli Infection",
                "remedy": "Most E. coli infections are self-limiting and require mainly supportive care with fluid and electrolyte replacement. Antibiotics are generally NOT recommended for Shiga toxin-producing E. coli (STEC/EnteroHemorrhagic E. coli) as they increase the risk of Hemolytic Uremic Syndrome (HUS). However, some non-Shiga-producing strains respond to fluoroquinolones. Seek urgent care if blood is present in stool, as this may indicate STEC infection. Platelet count and renal function monitoring is crucial for at-risk patients.",
                "bio_profile": {
                    "Sodium_mmol_L": 132.5,
                    "Potassium_mmol_L": 3.2,
                    "Chloride_mmol_L": 93.5,
                    "WBC_109_per_L": 10.75,
                    "Hemoglobin_g_dL": 12.2,
                    "Platelets_109_per_L": 188.0,
                    "Urea_mg_dL": 40.0,
                    "Creatinine_mg_dL": 1.25,
                    "Bilirubin_mg_dL": 0.8,
                    "ALT_U_L": 28.0,
                    "AST_U_L": 32.0
                }
            }
        ]

        for disease in diseases:
            obj, created = DiseaseInfo.objects.update_or_create(
                name=disease['name'],
                defaults={
                    'remedy': disease['remedy'],
                    'bio_profile': json.dumps(disease['bio_profile'])
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created {disease["name"]}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Updated existing {disease["name"]}')
                )

        self.stdout.write(
            self.style.SUCCESS('All waterborne diseases have been populated successfully!')
        )
