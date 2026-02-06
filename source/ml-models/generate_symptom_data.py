
import pandas as pd
import random

# Disease Definitions (Based on general medical knowledge)
# Symptoms, Common Water Characteristics, Disease Label

diseases = {
    'Cholera': {
        'symptoms': [
            'severe watery diarrhea', 'leg cramps', 'vomiting', 'dehydration', 'rapid heart rate', 
            'loss of skin elasticity', 'low blood pressure', 'thirst', 'muscle cramps'
        ],
        'water_color': ['Cloudy', 'Pale', 'Clear'], # Can be in clear water too
        'water_odor': ['Fishy', 'None', 'Rotten']
    },
    'Typhoid': {
        'symptoms': [
            'prolonged high fever', 'weakness', 'stomach pain', 'headache', 'loss of appetite', 
            'rash', 'constipation', 'diarrhea', 'fatigue'
        ],
        'water_color': ['Yellowish', 'Brown', 'Cloudy'],
        'water_odor': ['Sewage', 'Foul', 'None']
    },
    'Hepatitis A': {
        'symptoms': [
            'yellow skin or eyes', 'jaundice', 'dark urine', 'nausea', 'vomiting', 
            'abdominal pain', 'fever', 'light-colored stool', 'joint pain'
        ],
        'water_color': ['Yellowish', 'Brown', 'Clear'],
        'water_odor': ['Earthy', 'Foul', 'None']
    },
    'Dysentery': {
        'symptoms': [
            'bloody diarrhea', 'stomach cramps', 'fever', 'nausea', 'vomiting', 
            'mucus in stool', 'painful passing of stool'
        ],
        'water_color': ['Brown', 'Cloudy', 'Turbid'],
        'water_odor': ['Fecal', 'Rotten', 'Foul']
    },
    'Giardiasis': {
        'symptoms': [
            'watery diarrhea', 'greasy stool', 'stomach cramps', 'gas', 'nausea', 
            'dehydration', 'floating stool'
        ],
        'water_color': ['Clear', 'Cloudy'],
        'water_odor': ['Sulfur', 'Rotten Egg', 'Foul']
    },
    'E. coli Infection': {
        'symptoms': [
            'severe stomach cramps', 'bloody diarrhea', 'vomiting', 'nausea', 'mild fever'
        ],
        'water_color': ['Brown', 'Cloudy', 'Yellowish'],
        'water_odor': ['Fecal', 'Sewage', 'None']
    },
    'Leptospirosis': {
        'symptoms': [
            'high fever', 'headache', 'chills', 'muscle aches', 'vomiting', 
            'jaundice', 'red eyes', 'abdominal pain'
        ],
        'water_color': ['Muddy', 'Brown', 'Yellowish'],
        'water_odor': ['Earthy', 'Stagnant', 'None']
    },
    'Shigellosis': {
        'symptoms': [
            'diarrhea (bloody)', 'fever', 'stomach pain', 'feeling need to pass stool'
        ],
        'water_color': ['Cloudy', 'Brown'],
        'water_odor': ['Foul', 'Fecal', 'None']
    },
    'Healthy': {
        'symptoms': [
            'none', 'feeling good', 'healthy', 'normal', 'no pain', 'active'
        ],
        'water_color': ['Clear'],
        'water_odor': ['None']
    }
}

data = []

# Generate 500 samples per disease
samples_per_disease = 500

for disease, info in diseases.items():
    for _ in range(samples_per_disease):
        # Pick 2-4 random symptoms to make a description
        num_symptoms = random.randint(2, 4)
        selected_symptoms = random.sample(info['symptoms'], min(num_symptoms, len(info['symptoms'])))
        symptom_text = ", ".join(selected_symptoms)
        
        # Pick random water characteristics
        color = random.choice(info['water_color'])
        odor = random.choice(info['water_odor'])
        
        data.append({
            'Symptom_Text': symptom_text,
            'Water_Color': color,
            'Water_Odor': odor,
            'Disease': disease
        })

df = pd.DataFrame(data)
df.to_csv(r'd:\PY26112\MLnotebooks\symptom_data.csv', index=False)
print("Data generated successfully: d:\\PY26112\\MLnotebooks\\symptom_data.csv")
