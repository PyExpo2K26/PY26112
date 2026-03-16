import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Generate 500 rows of synthetic data
np.random.seed(42)
n_samples = 500

data = {
    'diarrhea_cases': np.random.randint(0, 50, n_samples),
    'vomiting_cases': np.random.randint(0, 50, n_samples),
    'fever_cases': np.random.randint(0, 50, n_samples),
    'water_ph': np.random.uniform(5.5, 9.0, n_samples),
    'water_turbidity': np.random.uniform(0.5, 10.0, n_samples),
    'rainfall_mm': np.random.uniform(0, 200, n_samples),
    'dissolved_oxygen': np.random.uniform(2.0, 10.0, n_samples),
    'bod': np.random.uniform(0.1, 15.0, n_samples),
    'cod': np.random.uniform(5.0, 50.0, n_samples),
    'nitrite': np.random.uniform(0.0, 5.0, n_samples),
    'ammonia': np.random.uniform(0.0, 5.0, n_samples),
    'fluoride': np.random.uniform(0.1, 3.0, n_samples),
    'chloride': np.random.uniform(10.0, 500.0, n_samples),
    'sulphate': np.random.uniform(10.0, 500.0, n_samples),
    'lead': np.random.uniform(0.0, 0.1, n_samples),
    'arsenic': np.random.uniform(0.0, 0.1, n_samples),
    'mercury': np.random.uniform(0.0, 0.05, n_samples),
    'cadmium': np.random.uniform(0.0, 0.05, n_samples),
    'iron': np.random.uniform(0.0, 5.0, n_samples),
}

df = pd.DataFrame(data)

# Risk logic (0=Low, 1=Medium, 2=High)


def calculate_risk(row):
    score = row['diarrhea_cases'] * 2 + row['vomiting_cases'] * 1.5 + row['water_turbidity'] * 3
    if row['water_ph'] < 6.5 or row['water_ph'] > 8.5:
        score += 20
        
    # Heavy Metal Penalties
    if row['lead'] > 0.01 or row['arsenic'] > 0.01 or row['mercury'] > 0.001 or row['cadmium'] > 0.003:
        score += 50

    if score > 120:
        return 2
    elif score > 60:
        return 1
    return 0


df['risk_level'] = df.apply(calculate_risk, axis=1)

X = df.drop('risk_level', axis=1)
y = df['risk_level']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model to the backend directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(base_dir, exist_ok=True)

model_path = os.path.join(base_dir, 'model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved successfully to {model_path}")
