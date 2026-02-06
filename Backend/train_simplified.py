
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load data
data_path = r'd:\PY26112\MLnotebooks\Content\data.csv'
try:
    data = pd.read_csv(data_path)
except FileNotFoundError:
    # Fallback/Debugging
    print(f"File not found at {data_path}")
    exit(1)

# Drop Symptoms if present (as per notebook logic)
if 'Symptoms_Text' in data.columns:
    data.drop(columns=['Symptoms_Text'], inplace=True)

# Encoders
le_gender = LabelEncoder()
le_water = LabelEncoder()
le_disease = LabelEncoder()

# Fit encoders (consistent with notebook alphabetical order usually, but explicit fits used here)
# WE MUST SAVE THESE MAPPINGS OR ENCODERS TO USE IN UTILS.PY
# OR just map manually: Female:0, Male:1 etc. based on unique values.

# Let's check unique values to be sure
# print(data['Gender'].unique())
# print(data['Water_Source'].unique())

data['Gender'] = le_gender.fit_transform(data['Gender'])
data['Water_Source'] = le_water.fit_transform(data['Water_Source'])
data['Disease'] = le_disease.fit_transform(data['Disease'])

# Define Features and Target
# Simplified Input Features: Age, Gender, Water_Source, Hygiene_Score
X = data[['Age', 'Gender', 'Water_Source', 'Hygiene_Score']]
y = data['Disease']

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Calculate Typical Profiles (Mean values for other columns per disease)
biochem_cols = [
    'Sodium_mmol_L', 'Potassium_mmol_L', 'Chloride_mmol_L', 'WBC_109_per_L', 
    'Hemoglobin_g_dL', 'Platelets_109_per_L', 'Urea_mg_dL', 'Creatinine_mg_dL', 
    'Bilirubin_mg_dL', 'ALT_U_L', 'AST_U_L'
]

profiles = data.groupby('Disease')[biochem_cols].mean().to_dict(orient='index')

# Mappings for reference
mappings = {
    'Gender': dict(zip(le_gender.classes_, le_gender.transform(le_gender.classes_))),
    'Water_Source': dict(zip(le_water.classes_, le_water.transform(le_water.classes_))),
    'Disease': dict(zip(le_disease.transform(le_disease.classes_), le_disease.classes_))
}

# Save artifacts
artifacts = {
    'model': model,
    'profiles': profiles,
    'mappings': mappings
}

output_path = r'd:\PY26112\MLnotebooks\simplified_model_artifacts.pkl'
with open(output_path, 'wb') as f:
    pickle.dump(artifacts, f)

print("Training complete. Artifacts saved.")
print("Mappings:", mappings)
