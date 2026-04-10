"""
Train a waterborne disease prediction model using symptom text and water quality indicators.
Uses TfidfVectorizer for symptom text and RandomForestClassifier for classification.
"""

import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import json

# Define paths
data_path = r'c:\PY26112\Backend\MLnotebooks\waterborne_disease_data.csv'
model_output_path = r'c:\PY26112\Backend\MLnotebooks\waterborne_disease_model.pkl'
artifacts_output_path = r'c:\PY26112\Backend\MLnotebooks\waterborne_artifacts.pkl'

# Load data
print("Loading waterborne disease data...")
try:
    data = pd.read_csv(data_path)
    print(f"Data loaded successfully. Shape: {data.shape}")
except FileNotFoundError:
    print(f"File not found at {data_path}")
    exit(1)

# Handle missing values
data.fillna('None', inplace=True)

# Prepare encoders for categorical features
le_gender = LabelEncoder()
le_water_source = LabelEncoder()
le_water_color = LabelEncoder()
le_water_odor = LabelEncoder()
le_disease = LabelEncoder()

# Fit encoders
data['Gender_Encoded'] = le_gender.fit_transform(data['Gender'])
data['Water_Source_Encoded'] = le_water_source.fit_transform(data['Water_Source'])
data['Water_Color_Encoded'] = le_water_color.fit_transform(data['Water_Color'])
data['Water_Odor_Encoded'] = le_water_odor.fit_transform(data['Water_Odor'])
data['Disease_Encoded'] = le_disease.fit_transform(data['Disease'])

print(f"Diseases: {le_disease.classes_}")
print(f"Water Colors: {le_water_color.classes_}")
print(f"Water Odors: {le_water_odor.classes_}")
print(f"Genders: {le_gender.classes_}")
print(f"Water Sources: {le_water_source.classes_}")

# Custom transformer to handle clinical features
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

# Create features
print("\nPreparing features...")

# Prepare target
y = data['Disease_Encoded']

# Split data
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2, random_state=42, stratify=y)

# Train Text Vectorizer on symptom text
print("Vectorizing symptom text...")
tfidf = TfidfVectorizer(max_features=100, ngram_range=(1, 2), stop_words='english')
X_train_text = tfidf.fit_transform(X_train['Symptom_Text'])
X_test_text = tfidf.transform(X_test['Symptom_Text'])

# Transform clinical features
print("Transforming clinical features...")
clinical_transformer = ClinicalFeatureTransformer()
X_train_clinical = clinical_transformer.fit_transform(X_train)
X_test_clinical = clinical_transformer.transform(X_test)

# Combine features
print("Combining features...")
from scipy.sparse import hstack
X_train_combined = hstack([X_train_text, X_train_clinical])
X_test_combined = hstack([X_test_text, X_test_clinical])

# Train Random Forest classifier
print("Training Random Forest classifier...")
model = RandomForestClassifier(n_estimators=150, max_depth=20, random_state=42, n_jobs=-1)
model.fit(X_train_combined, y_train)

# Evaluate
train_score = model.score(X_train_combined, y_train)
test_score = model.score(X_test_combined, y_test)
print(f"Training accuracy: {train_score:.4f}")
print(f"Testing accuracy: {test_score:.4f}")

# Calculate biochemical profiles per disease
print("\nCalculating biochemical profiles...")
biochem_cols = [
    'Sodium_mmol_L', 'Potassium_mmol_L', 'Chloride_mmol_L', 'WBC_109_per_L',
    'Hemoglobin_g_dL', 'Platelets_109_per_L', 'Urea_mg_dL', 'Creatinine_mg_dL',
    'Bilirubin_mg_dL', 'ALT_U_L', 'AST_U_L'
]

profiles = {}
for disease in le_disease.classes_:
    disease_data = data[data['Disease'] == disease]
    profile = {}
    for col in biochem_cols:
        profile[col] = float(disease_data[col].mean())
    profiles[disease] = profile

print("Profiles calculated for diseases:", list(profiles.keys()))

# Save artifacts
print("\nSaving model and artifacts...")
artifacts = {
    'model': model,
    'tfidf': tfidf,
    'clinical_transformer': clinical_transformer,
    'profiles': profiles,
    'disease_encoder': le_disease,
    'gender_encoder': le_gender,
    'water_source_encoder': le_water_source,
    'water_color_encoder': le_water_color,
    'water_odor_encoder': le_water_odor,
    'disease_classes': le_disease.classes_,
    'water_color_classes': le_water_color.classes_,
    'water_odor_classes': le_water_odor.classes_,
}

with open(artifacts_output_path, 'wb') as f:
    pickle.dump(artifacts, f)

print(f"Artifacts saved to {artifacts_output_path}")

# Also save model separately for compatibility
with open(model_output_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved to {model_output_path}")
print("\nTraining complete!")
