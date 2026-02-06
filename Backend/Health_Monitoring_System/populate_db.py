import os
import django
import json

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Health_Monitoring_System.settings')
django.setup()

from web.models import DiseaseInfo

def populate():
    diseases = [
        {
            "name": "Cholera",
            "remedy": "Rehydration is the most important treatment. Rapidly replace fluids and electrolytes lost through diarrhea using Oral Rehydration Salts (ORS). In severe cases, intravenous fluids are required. Antibiotics can shorten the duration of the illness.",
            "bio_profile": {
                "Sodium_mmol_L": 132.0,
                "Potassium_mmol_L": 3.2,
                "Chloride_mmol_L": 95.0,
                "WBC_109_per_L": 12.5,
                "Hemoglobin_g_dL": 14.2,
                "Platelets_109_per_L": 210.0,
                "Urea_mg_dL": 45.0,
                "Creatinine_mg_dL": 1.4,
                "Bilirubin_mg_dL": 0.8,
                "ALT_U_L": 35.0,
                "AST_U_L": 40.0
            }
        },
        {
            "name": "Typhoid",
            "remedy": "Typhoid fever is treated with antibiotics such as ciprofloxacin or ceftriaxone. It is essential to complete the full course of antibiotics. Supportive care includes fluid replacement and a soft, easily digestible diet. Prevention via vaccination is highly recommended.",
            "bio_profile": {
                "Sodium_mmol_L": 135.0,
                "Potassium_mmol_L": 3.8,
                "Chloride_mmol_L": 98.0,
                "WBC_109_per_L": 3.5,
                "Hemoglobin_g_dL": 11.5,
                "Platelets_109_per_L": 140.0,
                "Urea_mg_dL": 30.0,
                "Creatinine_mg_dL": 0.9,
                "Bilirubin_mg_dL": 1.5,
                "ALT_U_L": 85.0,
                "AST_U_L": 75.0
            }
        },
        {
            "name": "Hepatitis A",
            "remedy": "There is no specific treatment for Hepatitis A. Management involves supportive care: rest, adequate nutrition, and fluids. Avoid alcohol and medications that can stress the liver (like acetaminophen) until recovery. Vaccination can prevent future infections.",
            "bio_profile": {
                "Sodium_mmol_L": 138.0,
                "Potassium_mmol_L": 4.1,
                "Chloride_mmol_L": 102.0,
                "WBC_109_per_L": 6.8,
                "Hemoglobin_g_dL": 13.5,
                "Platelets_109_per_L": 180.0,
                "Urea_mg_dL": 25.0,
                "Creatinine_mg_dL": 0.8,
                "Bilirubin_mg_dL": 4.5,
                "ALT_U_L": 850.0,
                "AST_U_L": 720.0
            }
        },
        {
            "name": "Dysentery",
            "remedy": "Treatment focuses on replacing lost fluids. Antibiotics (e.g., ciprofloxacin) are used for bacterial dysentery (Shigellosis), while amoebicidal drugs (e.g., metronidazole) are used for amoebic dysentery. Avoid anti-diarrheal medications which can worsen the condition.",
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
            "remedy": "Metronidazole, tinidazole, or nitazoxanide are the preferred antibiotics. Ensure good hydration. Practice strict hand hygiene to prevent spread within households.",
            "bio_profile": {
                "Sodium_mmol_L": 140.0,
                "Potassium_mmol_L": 4.2,
                "Chloride_mmol_L": 104.0,
                "WBC_109_per_L": 7.5,
                "Hemoglobin_g_dL": 13.0,
                "Platelets_109_per_L": 220.0,
                "Urea_mg_dL": 28.0,
                "Creatinine_mg_dL": 0.9,
                "Bilirubin_mg_dL": 0.6,
                "ALT_U_L": 25.0,
                "AST_U_L": 22.0
            }
        },
        {
            "name": "E. coli Infection",
            "remedy": "Most E. coli infections resolve with rest and fluids. Avoid antibiotics for Shiga toxin-producing E. coli (STEC) as they may increase the risk of Hemolytic Uremic Syndrome (HUS). Seek urgent care if blood is present in stool.",
            "bio_profile": {
                "Sodium_mmol_L": 137.0,
                "Potassium_mmol_L": 3.9,
                "Chloride_mmol_L": 101.0,
                "WBC_109_per_L": 11.0,
                "Hemoglobin_g_dL": 12.5,
                "Platelets_109_per_L": 190.0,
                "Urea_mg_dL": 40.0,
                "Creatinine_mg_dL": 1.2,
                "Bilirubin_mg_dL": 0.9,
                "ALT_U_L": 40.0,
                "AST_U_L": 38.0
            }
        },
        {
            "name": "Leptospirosis",
            "remedy": "Treat with antibiotics such as doxycycline or penicillin early in the course of the illness. Severe cases may require intravenous antibiotics and supportive care in a hospital setting.",
            "bio_profile": {
                "Sodium_mmol_L": 134.0,
                "Potassium_mmol_L": 3.6,
                "Chloride_mmol_L": 96.0,
                "WBC_109_per_L": 15.5,
                "Hemoglobin_g_dL": 11.0,
                "Platelets_109_per_L": 85.0,
                "Urea_mg_dL": 65.0,
                "Creatinine_mg_dL": 2.2,
                "Bilirubin_mg_dL": 3.8,
                "ALT_U_L": 120.0,
                "AST_U_L": 110.0
            }
        },
        {
            "name": "Shigellosis",
            "remedy": "Mild cases usually settle without treatment. In more severe cases, antibiotics like ciprofloxacin or azithromycin can shorten the illness. Hydration is key.",
            "bio_profile": {
                "Sodium_mmol_L": 135.0,
                "Potassium_mmol_L": 3.4,
                "Chloride_mmol_L": 97.0,
                "WBC_109_per_L": 16.0,
                "Hemoglobin_g_dL": 12.0,
                "Platelets_109_per_L": 280.0,
                "Urea_mg_dL": 32.0,
                "Creatinine_mg_dL": 1.0,
                "Bilirubin_mg_dL": 0.8,
                "ALT_U_L": 35.0,
                "AST_U_L": 36.0
            }
        },
        {
            "name": "Healthy",
            "remedy": "Maintain good hygiene, drink clean water, and follow a balanced diet. No treatment necessary.",
            "bio_profile": {
                "Sodium_mmol_L": 140.0,
                "Potassium_mmol_L": 4.5,
                "Chloride_mmol_L": 105.0,
                "WBC_109_per_L": 7.0,
                "Hemoglobin_g_dL": 14.5,
                "Platelets_109_per_L": 250.0,
                "Urea_mg_dL": 20.0,
                "Creatinine_mg_dL": 0.9,
                "Bilirubin_mg_dL": 0.5,
                "ALT_U_L": 20.0,
                "AST_U_L": 18.0
            }
        }
    ]

    for d in diseases:
        obj, created = DiseaseInfo.objects.update_or_create(
            name=d["name"],
            defaults={
                "remedy": d["remedy"],
                "bio_profile": json.dumps(d["bio_profile"])
            }
        )
        status = "Created" if created else "Updated"
        print(f"{status}: {obj.name}")

if __name__ == "__main__":
    populate()
