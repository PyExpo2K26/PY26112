
import pickle
import os
import pandas as pd
import numpy as np
from scipy.sparse import hstack
from sklearn.base import BaseEstimator, TransformerMixin

# Define model paths
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
WATERBORNE_ARTIFACTS_PATH = BASE_DIR.parent / 'ml-models' / 'artifacts' / 'waterborne_artifacts.pkl'

# Global variables to cache loaded artifacts
_artifacts = None

class ClinicalFeatureTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Extract Age, Gender, Water_Source, Hygiene_Score, Water_Color, Water_Odor
        features = []
        for idx, row in X.iterrows():
            water_color_code = row.get('Water_Color_Encoded', 0)
            water_odor_code = row.get('Water_Odor_Encoded', 0)
            gender_code = row.get('Gender_Encoded', 0)
            water_source_code = row.get('Water_Source_Encoded', 0)
            
            feature_vector = [
                float(row.get('Age', 0)),
                float(gender_code),
                float(water_source_code),
                float(row.get('Hygiene_Score', 0)),
                float(water_color_code),
                float(water_odor_code)
            ]
            features.append(feature_vector)
        return np.array(features, dtype=np.float64)

class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'Health_Monitoring_System.web.models':
            module = 'web.models'
        elif module == 'backend.web.models':
            module = 'web.models'
        elif module == '__main__' and name == 'ClinicalFeatureTransformer':
            return ClinicalFeatureTransformer
            
        try:
            return super().find_class(module, name)
        except Exception as e:
            # Fallback for unexpected module movements
            if name == 'DiseaseInfo':
                from .models import DiseaseInfo
                return DiseaseInfo
            raise

def load_artifacts():
    """Load the trained waterborne disease model artifacts."""
    global _artifacts
    if _artifacts is None:
        try:
            with open(WATERBORNE_ARTIFACTS_PATH, 'rb') as f:
                # Use custom unpickler to handle module movements
                _artifacts = CustomUnpickler(f).load()
            print("Artifacts loaded successfully")
        except Exception as e:
            import traceback
            print(f"Error loading artifacts: {traceback.format_exc()}")
            return None
    return _artifacts

def make_prediction(data_dict):
    """
    Predict waterborne disease based on symptom text and water quality indicators.
    
    data_dict should contain: 'Symptom_Text', 'Water_Color', 'Water_Odor'
    Optional: 'Age', 'Gender', 'Water_Source', 'Hygiene_Score'
    """
    artifacts = load_artifacts()
    if not artifacts:
        return "Model not loaded", "", {}

    try:
        # Extract and prepare input data
        symptom_text = data_dict.get('Symptom_Text', '')
        water_color = data_dict.get('Water_Color', 'Clear')
        water_odor = data_dict.get('Water_Odor', 'None')
        age = data_dict.get('Age', 25)
        gender = data_dict.get('Gender', 'Male')
        water_source = data_dict.get('Water_Source', 'Tap')
        hygiene_score = data_dict.get('Hygiene_Score', 3)
        
        # Load encoders
        gender_encoder = artifacts.get('gender_encoder')
        water_source_encoder = artifacts.get('water_source_encoder')
        water_color_encoder = artifacts.get('water_color_encoder')
        water_odor_encoder = artifacts.get('water_odor_encoder')
        disease_encoder = artifacts.get('disease_encoder')
        tfidf = artifacts.get('tfidf')
        model = artifacts.get('model')
        profiles = artifacts.get('profiles')
        
        if not all([gender_encoder, water_source_encoder, water_color_encoder, 
                   water_odor_encoder, disease_encoder, tfidf, model, profiles]):
            return "Model components missing", "", {}
        
        # Encode categorical features
        try:
            gender_code = gender_encoder.transform([gender])[0]
        except:
            gender_code = 0
        
        try:
            water_source_code = water_source_encoder.transform([water_source])[0]
        except:
            water_source_code = 0
        
        try:
            water_color_code = water_color_encoder.transform([water_color])[0]
        except:
            water_color_code = 0
        
        try:
            water_odor_code = water_odor_encoder.transform([water_odor])[0]
        except:
            water_odor_code = 0
        
        # Process text with TF-IDF
        X_text = tfidf.transform([symptom_text])
        
        # Create clinical features
        X_clinical = np.array([[
            float(age),
            float(gender_code),
            float(water_source_code),
            float(hygiene_score),
            float(water_color_code),
            float(water_odor_code)
        ]], dtype=np.float64)
        
        # Combine all features
        X_combined = hstack([X_text, X_clinical])
        
        # Make prediction
        disease_encoded = model.predict(X_combined)[0]
        disease_name = disease_encoder.inverse_transform([disease_encoded])[0]
        
        # Fetch biochemical info from DB if available
        remedy = "Consult a doctor for proper treatment"
        bio_info = {}
        
        try:
            from .models import DiseaseInfo
            import json
            
            info = DiseaseInfo.objects.get(name__iexact=disease_name)
            remedy = info.remedy
            
            # Parse bio profile
            raw_bio_info = json.loads(info.bio_profile) if info.bio_profile else {}
            
            # Format keys for display
            bio_info = {}
            for k, v in raw_bio_info.items():
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
            remedy = f"Consult a doctor. {disease_name} detected but not yet in database."
            # Use profiles from model if available
            if disease_name in profiles:
                profile = profiles[disease_name]
                bio_info = {}
                for k, v in profile.items():
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
        
        return disease_name, remedy, bio_info
        
    except Exception as e:
        import traceback
        print(f"Error in prediction: {traceback.format_exc()}")
        return f"Error: {str(e)}", "", {}
