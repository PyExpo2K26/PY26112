# Machine Learning Model Documentation

## Overview

The Waterborne Disease Prediction System uses a Random Forest classifier combined with TF-IDF text vectorization to predict waterborne diseases based on symptom descriptions and water quality indicators.

## Model Architecture

### Components

1. **Text Processor**: TF-IDF Vectorizer
2. **Clinical Feature Extractor**: Numerical and categorical features
3. **Classifier**: Random Forest (150 estimators)
4. **Encoder Set**: Label encoders for categorical variables

### Features

#### Text Features (100 features)
- **Input**: Symptom_Text
- **Processing**: TF-IDF Vectorization
  - Max features: 100
  - N-gram range: (1, 2) - unigrams and bigrams
  - Stop words: English
  - Min document frequency: 1
- **Example**: "watery diarrhea vomiting" → 100-dimensional TF-IDF vector

#### Clinical Features (6 features)
1. **Age** (numerical) - Range: 6-62 years
2. **Gender** (encoded) - Female (0), Male (1)
3. **Water_Source** (encoded) - River (0), Tap (1), Well (2)
4. **Hygiene_Score** (numerical) - Range: 1-5
5. **Water_Color** (encoded) - Clear (0), Turbid (1)
6. **Water_Odor** (encoded) - None (0), Fishy (1), Musty (2)

**Total Features**: 106 (100 text + 6 clinical)

## Training Data

### Dataset: `waterborne_disease_data.csv`
- **Samples**: 54 instances
- **Classes**: 6 waterborne diseases
- **Features**: 19 columns
- **Target Distribution**:
  - Cholera: 9 samples (16.7%)
  - Dysentery: 9 samples (16.7%)
  - E. coli Infection: 9 samples (16.7%)
  - Giardiasis: 9 samples (16.7%)
  - Hepatitis A: 9 samples (16.7%)
  - Typhoid: 9 samples (16.7%)

### Data Collection
- Synthetic data based on medical literature
- Realistic symptom combinations
- Biochemical value ranges from clinical studies
- Diverse demographics and water conditions

### Data Columns
```
Age                          - Patient age
Gender                       - Male/Female
Water_Source                 - River/Tap/Well
Hygiene_Score                - 1-5 scale
Symptom_Text                 - Free text description
Water_Color                  - Clear/Turbid
Water_Odor                   - None/Fishy/Musty
Sodium_mmol_L                - Electrolyte level
Potassium_mmol_L             - Electrolyte level
Chloride_mmol_L              - Electrolyte level
WBC_109_per_L                - White blood cell count
Hemoglobin_g_dL              - Hemoglobin concentration
Platelets_109_per_L          - Platelet count
Urea_mg_dL                   - Kidney function marker
Creatinine_mg_dL             - Kidney function marker
Bilirubin_mg_dL              - Liver function marker
ALT_U_L                      - Liver enzyme
AST_U_L                      - Liver enzyme
Disease                      - Target variable
```

## Training Process

### 1. Data Loading & Preprocessing
```python
# Load CSV
data = pd.read_csv('waterborne_disease_data.csv')

# Fill missing values
data.fillna('None', inplace=True)

# Handle categorical variables
le_gender = LabelEncoder()
le_water_source = LabelEncoder()
le_water_color = LabelEncoder()
le_water_odor = LabelEncoder()
le_disease = LabelEncoder()
```

### 2. Feature Engineering
```python
# Text features
tfidf = TfidfVectorizer(max_features=100, ngram_range=(1, 2))
X_text = tfidf.fit_transform(data['Symptom_Text'])

# Clinical features
X_clinical = np.array([
    age, gender_encoded, water_source_encoded, 
    hygiene_score, water_color_encoded, water_odor_encoded
])

# Combine features
X_combined = hstack([X_text, X_clinical])
y = le_disease.fit_transform(data['Disease'])
```

### 3. Train-Test Split
```python
X_train, X_test, y_train, y_test = train_test_split(
    X_combined, y, 
    test_size=0.2,  # 20% test
    random_state=42,
    stratify=y
)
```

Training: 43 samples (80%)  
Testing: 11 samples (20%)

### 4. Model Training
```python
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)
```

**Hyperparameters**:
- Estimators: 150 trees
- Max depth: 20 levels
- Random state: 42 (reproducibility)
- Jobs: -1 (use all processors)

### 5. Validation
```python
train_score = model.score(X_train, y_train)  # 1.0000 (100%)
test_score = model.score(X_test, y_test)    # 0.7273 (72.73%)
```

## Model Performance

### Accuracy Metrics
- **Training Accuracy**: 100% (43/43 correct)
- **Testing Accuracy**: 72.73% (8/11 correct)
- **Confusion Matrix**: Shows disease classification performance

### Strengths
1. Excellent training performance indicates good feature engineering
2. Captures complex patterns in symptom combinations
3. Handles multiple input modalities (text + numerical)
4. Robust to feature scaling variations

### Limitations
1. Small dataset (54 samples) - prone to overfitting
2. Test accuracy (72.73%) suggests room for improvement
3. May not generalize well to out-of-distribution symptoms
4. Synthetic data - may not capture real-world variability

## Biochemical Profiles

Each disease has computed average biochemical values from training data:

### Cholera Profile
```
Sodium: 130.5 mmol/L (electrolyte loss)
Potassium: 3.1 mmol/L (severe depletion)
Chloride: 92.5 mmol/L (severe loss)
WBC: 13.5 × 10^9/L (elevated - infection)
Hemoglobin: 13.8 g/dL (normal to high - hemoconcentration)
Platelets: 210 × 10^9/L (normal)
Urea: 48.0 mg/dL (elevated - dehydration)
Creatinine: 1.5 mg/dL (mildly elevated)
```

### Hepatitis A Profile
```
Sodium: 139.0 mmol/L (normal)
Potassium: 4.2 mmol/L (normal)
Chloride: 102.5 mmol/L (normal)
WBC: 7.0 × 10^9/L (normal)
Hemoglobin: 13.2 g/dL (normal)
Platelets: 178 × 10^9/L (normal to low)
Bilirubin: 4.5 mg/dL (highly elevated - jaundice)
ALT: 847 U/L (severely elevated - liver damage)
AST: 725 U/L (severely elevated - liver damage)
```

## Prediction Process

### Input Processing
1. Receive symptom text and water quality indicators
2. Encode categorical inputs using saved encoders
3. Vectorize symptom text with saved TF-IDF model
4. Combine features into 106-dimensional vector

### Classification
1. Feed feature vector to Random Forest model
2. Get predicted disease class
3. Return disease name and biochemical profile

### Output
```
Disease: Cholera
Confidence: 0.87 (87% of trees vote for Cholera)
Remedy: [Retrieved from database]
Biochemical Profile: [Computed average values]
```

## Model Artifacts

Saved in `waterborne_artifacts.pkl`:
```python
{
    'model': RandomForestClassifier,
    'tfidf': TfidfVectorizer,
    'profiles': dict,  # Disease -> biochemical values
    'disease_encoder': LabelEncoder,
    'gender_encoder': LabelEncoder,
    'water_source_encoder': LabelEncoder,
    'water_color_encoder': LabelEncoder,
    'water_odor_encoder': LabelEncoder,
}
```

## Feature Importance

Top TF-IDF features (example):
1. "severe diarrhea" - strong indicator of cholera
2. "high fever" - indicator of typhoid
3. "jaundice" - strong indicator of hepatitis
4. "bloody diarrhea" - indicates dysentery/E. coli
5. "watery diarrhea" - broad indicator

## Cross-Validation

Recommended for better performance estimates:
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_combined, y, cv=5)
print(f"CV Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

## Handling Edge Cases

### Unknown Words in Symptoms
- TF-IDF automatically handles unknown words (zero vector)
- Model trained on diverse symptom vocabulary

### Missing Clinical Features
- Defaults used: Age=25, Gender=Male, Water_Source=Tap, Hygiene=3
- Model generalizes from small feature set

### Out-of-Range Values
- Clipping: Values beyond training range clipped to min/max
- Normalization: Features automatically normalized by TF-IDF

## Improvements for Future Versions

1. **Data Collection**
   - Increase dataset to 1000+ samples
   - Include real-world patient data
   - Collect seasonal variations

2. **Model Enhancement**
   - Ensemble with gradient boosting
   - Deep learning (LSTM for sequence patterns)
   - Class weights for imbalanced data

3. **Feature Engineering**
   - Word embeddings instead of TF-IDF
   - Domain-specific medical vocabularies
   - Time-series features for epidemics

4. **Validation**
   - Cross-validation with stratification
   - Evaluation on real patient data
   - ROC-AUC analysis per disease

5. **Deployment**
   - Model versioning and tracking
   - A/B testing for model updates
   - Monitoring and retraining pipeline

## References

- Scikit-learn RandomForest: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- TF-IDF Documentation: https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
- Waterborne Diseases: WHO and CDC guidelines

---

**Model Version**: 1.0  
**Training Date**: February 6, 2026  
**Framework**: scikit-learn  
**Python Version**: 3.13.7
