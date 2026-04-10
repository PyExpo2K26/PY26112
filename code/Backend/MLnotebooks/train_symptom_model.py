
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

# Load data
data_path = r'd:\PY26112\MLnotebooks\symptom_data.csv'
data = pd.read_csv(data_path)

# Features: Symptom_Text (Text), Water_Color (Cat), Water_Odor (Cat)
# Target: Disease

X = data[['Symptom_Text', 'Water_Color', 'Water_Odor']]
y = data['Disease']

# Preprocessing Pipeline
# Text columns use CountVectorizer
# Categorical columns use OneHotEncoder

preprocessor = ColumnTransformer(
    transformers=[
        ('text', Pipeline([
            ('vect', CountVectorizer(stop_words='english')),
            ('tfidf', TfidfTransformer()),
        ]), 'Symptom_Text'),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Water_Color', 'Water_Odor'])
    ]
)

# Model Pipeline
clf = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)) 
    # SGD with hinge is SVM-like, good for text. Or maybe RandomForest for combined features?
    # Let's use RandomForest as it handles mixed types reasonably well once transformed
])

# Let's switch to RandomForest at the end for robustness
clf = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

clf.fit(X, y)

# Save the model
model_path = r'd:\PY26112\MLnotebooks\symptom_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(clf, f)

print("Symptom model trained and saved to:", model_path)
