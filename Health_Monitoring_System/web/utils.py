
import pickle
import os
import pandas as pd
import numpy as np

# Define mappings based on training data analysis
GENDER_MAP = {'Female': 0, 'Male': 1}
WATER_SOURCE_MAP = {'Bottled': 0, 'River': 1, 'Tap': 2, 'Well': 3}

MODEL_PATH = r'd:\PY26112\MLnotebooks\symptom_model.pkl'

_model = None

def load_model():
    global _model
    if _model is None:
        try:
            with open(MODEL_PATH, 'rb') as f:
                _model = pickle.load(f)
        except Exception as e:
            print(f"Error loading model: {e}")
            return None
    return _model

def make_prediction(data_dict):
    """
    data_dict should contain: 'Symptom_Text', 'Water_Color', 'Water_Odor'
    """
    model = load_model()
    if not model:
        return "Model not loaded", "", {}

    try:
        # Prepare DataFrame for pipeline
        # Ensure 'Symptom_Text' is a string, defaulting to empty if None
        symptom_text = data_dict.get('Symptom_Text') or ""
        
        # We need to reconstruct the dataframe with safe values
        safe_data = {
            'Symptom_Text': symptom_text,
            'Water_Color': data_dict.get('Water_Color', 'Clear'),
            'Water_Odor': data_dict.get('Water_Odor', 'None')
        }
        
        df = pd.DataFrame([safe_data])
        
        # Predict Disease
        disease_name = model.predict(df)[0]
        
        # Fetch Info from DB
        # We need to import model here to ensure AppRegistry is ready
        from .models import DiseaseInfo
        import json
        
        try:
            info = DiseaseInfo.objects.get(name=disease_name)
            remedy = info.remedy
            # Get Biochemical Info
            # Assuming 'profiles' and 'pred_code' are defined elsewhere or passed in context
            # For this edit, we'll assume info.bio_profile is the source for raw_bio_info
            raw_bio_info = json.loads(info.bio_profile) if info.bio_profile else {}
            
            # Format keys for display
            bio_info = {}
            for k, v in raw_bio_info.items():
                # Example: Sodium_mmol_L -> Sodium (mmol/L)
                clean_key = k.replace('_', ' ')
                if 'mmol L' in clean_key:
                    clean_key = clean_key.replace('mmol L', '(mmol/L)')
                elif 'mg dL' in clean_key:
                    clean_key = clean_key.replace('mg dL', '(mg/dL)')
                elif 'U L' in clean_key:
                    clean_key = clean_key.replace('U L', '(U/L)')
                elif '109 per L' in clean_key:
                     clean_key = clean_key.replace('109 per L', '(10^9/L)')
                elif 'g dL' in clean_key:
                    clean_key = clean_key.replace('g dL', '(g/dL)')
                    
                bio_info[clean_key] = v
            
        except DiseaseInfo.DoesNotExist:
            remedy = "Consult a doctor. No specific remedy found in database."
            bio_info = {} # Initialize bio_info even if disease not found
        
        return disease_name, remedy, bio_info
        
    except Exception as e:
        return f"Error: {str(e)}", "", {}
