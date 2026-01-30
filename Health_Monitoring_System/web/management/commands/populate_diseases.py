
import json
import pickle
from django.core.management.base import BaseCommand
from web.models import DiseaseInfo

class Command(BaseCommand):
    help = 'Populates DiseaseInfo with initial data'

    def handle(self, *args, **kwargs):
        # Load biochemical profiles from previous artifacts
        artifacts_path = r'd:\PY26112\MLnotebooks\simplified_model_artifacts.pkl'
        try:
            with open(artifacts_path, 'rb') as f:
                artifacts = pickle.load(f)
                profiles = artifacts['profiles']
                
                # Disease encoder mapping (code -> name)
                # profiles keys are codes, we need names
                disease_map = artifacts['mappings']['Disease']
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading artifacts: {e}'))
            return

        # Remedies Database (Synthesized Knowledge)
        remedies = {
            'Cholera': "Oral Rehydration Salts (ORS), Zinc supplements, Antibiotics (doxycycline), Plenty of fluids.",
            'Typhoid': "Antibiotics (ciprofloxacin, azithromycin), Fluids, Rest, Bland diet.",
            'Hepatitis A': "Rest, Adequate nutrition, Fluids, Avoid alcohol. Vaccine is available for prevention.",
            'Dysentery': "Antibiotics, Amoebicides, Fluids, ORS. Avoid dairy products.",
            'Giardiasis': "Metronidazole or Tinidazole, Hydration. Wash hands frequently.",
            'E. coli Infection': "Hydration (Fluids/ORS), Rest. Avoid anti-diarrheal medication initially.",
            'Leptospirosis': "Antibiotics (doxycycline or penicillin). Severe cases require hospitalization.",
            'Shigellosis': "Antibiotics, Fluids to prevent dehydration. Frequent hand washing.",
            'Healthy': "No remedy nreede. Maintain good hydration and hygiene.",
            'Unknown': "Consult a doctor."
        }
        
        # Determine Bio Profile for each disease
        # profiles is {code: {bio_dict}}
        # disease_map is {code: name}
        
        for code, bio_data in profiles.items():
            name = disease_map.get(code)
            if not name:
                continue
                
            remedy = remedies.get(name, "Consult a doctor.")
            
            # Format bio_profile as string
            bio_str = json.dumps(bio_data, indent=2)
            
            DiseaseInfo.objects.update_or_create(
                name=name,
                defaults={
                    'remedy': remedy,
                    'bio_profile': bio_str
                }
            )
            self.stdout.write(f'Updated/Created: {name}')
            
        # Ensure Healthy exists if not in profiles
        if 'Healthy' not in [disease_map.get(c) for c in profiles.keys()]:
             DiseaseInfo.objects.update_or_create(
                name='Healthy',
                defaults={
                    'remedy': remedies['Healthy'],
                    'bio_profile': json.dumps({"Status": "Normal Parameters"})
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated DiseaseInfo'))
