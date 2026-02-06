# ML Models Directory Structure

## Overview
Professional organization of all machine learning components for the Waterborne Disease Health Monitoring System.

## Directory Hierarchy

```
ml-models/
├── data/                           # Data Management
│   ├── training/                   # Training datasets
│   │   └── waterborne_disease_data.csv
│   │       ├── Purpose: Main training dataset for the waterborne disease model
│   │       ├── Records: 54 samples
│   │       ├── Features: 19 columns (age, gender, symptoms, biochemical, disease)
│   │       └── Format: CSV with headers
│   │
│   └── reference/                  # Reference and supplementary data
│       ├── symptom_data.csv
│       │   ├── Purpose: Reference symptom dataset
│       │   ├── Usage: Data generation and model comparison
│       │   └── Format: CSV
│       │
│       └── data.csv
│           ├── Purpose: General reference dataset
│           ├── Usage: Model validation and testing
│           └── Format: CSV
│
├── artifacts/                      # Trained Models & Serialized Objects
│   ├── waterborne_disease_model.pkl
│   │   ├── Type: Random Forest Classifier
│   │   ├── Estimators: 150 trees
│   │   ├── Features: 106 (100 TF-IDF + 6 clinical)
│   │   ├── Accuracy: 72.73% (test set)
│   │   └── Size: ~2MB
│   │
│   ├── waterborne_artifacts.pkl
│   │   ├── Contains: Complete model pipeline
│   │   ├── Components:
│   │   │   ├── Trained Random Forest model
│   │   │   ├── TF-IDF vectorizer
│   │   │   ├── Label encoders (gender, water source, color, odor, disease)
│   │   │   ├── Biochemical profiles per disease
│   │   │   └── Disease classes metadata
│   │   └── Size: ~3MB
│   │
│   ├── simplified_model_artifacts.pkl
│   │   ├── Type: Simplified model artifacts
│   │   └── Usage: Alternative model for testing
│   │
│   ├── symptom_model.pkl
│   │   ├── Type: Legacy symptom model
│   │   └── Status: Reference/archived
│   │
│   └── water_disease_model.pkl
│       ├── Type: Water-specific disease model
│       └── Status: Reference/archived
│
├── scripts/                        # Training and Data Processing Scripts
│   ├── train_waterborne_model.py
│   │   ├── Purpose: Main training script for waterborne disease model
│   │   ├── Input: data/training/waterborne_disease_data.csv
│   │   ├── Output: artifacts/waterborne_*.pkl
│   │   ├── Features:
│   │   │   ├── Data preprocessing
│   │   │   ├── Feature engineering (TF-IDF + clinical)
│   │   │   ├── Model training (Random Forest)
│   │   │   ├── Biochemical profile calculation
│   │   │   └── Artifact serialization
│   │   └── Dependencies: scikit-learn, pandas, numpy, scipy
│   │
│   ├── generate_symptom_data.py
│   │   ├── Purpose: Generate synthetic symptom data
│   │   ├── Output: data/reference/symptom_data.csv
│   │   └── Usage: Data generation for modeling
│   │
│   └── train_symptom_model.py
│       ├── Purpose: Train models on symptom data
│       ├── Input: data/reference/
│       └── Output: artifacts/
│
├── notebooks/                      # Jupyter Notebooks for Analysis
│   └── MLnote.ipynb
│       ├── Purpose: Exploratory data analysis and model documentation
│       ├── Contents:
│       │   ├── Data exploration
│       │   ├── Feature analysis
│       │   ├── Model training walkthrough
│       │   └── Results visualization
│       └── Status: Analysis reference
│
├── models/                         # Alternative: Future expanded model storage
│   ├── [Reserved for multiple models]
│   ├── [Versioned models]
│   └── [Experimental models]
│
└── README.md                       # This file - Directory documentation
```

## Data Files Detail

### Training Data: `waterborne_disease_data.csv`

**Location**: `ml-models/data/training/waterborne_disease_data.csv`

**Specifications**:
- **Rows**: 54 samples
- **Columns**: 19
- **Classes**: 6 waterborne diseases
- **Class Distribution**: Balanced (9 samples per disease)

**Column Details**:
```
Clinical Features:
- Age (int): 6-62 years
- Gender (str): Female/Male
- Water_Source (str): River/Tap/Well
- Hygiene_Score (int): 1-5 scale

Symptom Features:
- Symptom_Text (str): Free text description

Water Quality Features:
- Water_Color (str): Clear/Turbid
- Water_Odor (str): None/Fishy/Musty

Biochemical Features:
- Sodium_mmol_L (float)
- Potassium_mmol_L (float)
- Chloride_mmol_L (float)
- WBC_109_per_L (float)
- Hemoglobin_g_dL (float)
- Platelets_109_per_L (float)
- Urea_mg_dL (float)
- Creatinine_mg_dL (float)
- Bilirubin_mg_dL (float)
- ALT_U_L (float)
- AST_U_L (float)

Target:
- Disease (str): Disease classification
```

**Diseases Represented**:
1. Cholera
2. Dysentery
3. E. coli Infection
4. Giardiasis
5. Hepatitis A
6. Typhoid

### Reference Data

**symptom_data.csv**: Supplementary symptom dataset
- Purpose: Additional reference for symptom patterns
- Location: `ml-models/data/reference/`

**data.csv**: General reference dataset
- Purpose: Model validation and testing reference
- Location: `ml-models/data/reference/`

## Model Artifacts Detail

### Primary Model: `waterborne_artifacts.pkl`

**Serialized Contents**:
```python
{
    'model': RandomForestClassifier(),           # Trained classifier
    'tfidf': TfidfVectorizer(),                  # Text vectorizer
    'clinical_transformer': ClinicalFeatureTransformer(),
    'profiles': dict,                             # Biochemical profiles per disease
    'disease_encoder': LabelEncoder(),           # Disease label encoder
    'gender_encoder': LabelEncoder(),            # Gender label encoder
    'water_source_encoder': LabelEncoder(),      # Water source encoder
    'water_color_encoder': LabelEncoder(),       # Water color encoder
    'water_odor_encoder': LabelEncoder(),        # Water odor encoder
    'disease_classes': np.array(),               # Disease names
    'water_color_classes': np.array(),           # Color categories
    'water_odor_classes': np.array(),            # Odor categories
}
```

**Loading Usage**:
```python
import pickle

with open('artifacts/waterborne_artifacts.pkl', 'rb') as f:
    artifacts = pickle.load(f)

model = artifacts['model']
tfidf = artifacts['tfidf']
disease_encoder = artifacts['disease_encoder']
```

### Alternative Models

**waterborne_disease_model.pkl**: Standalone trained model
- Contains only the Random Forest classifier
- Lighter than complete artifacts
- Usage: Model inference only

**simplified_model_artifacts.pkl**: Simplified version
- Reduced feature set
- Faster inference
- Usage: Baseline comparison

## Script Usage

### Training Waterborne Model
```bash
python scripts/train_waterborne_model.py
```

**Process**:
1. Load training data from `data/training/waterborne_disease_data.csv`
2. Preprocess and encode categorical features
3. Vectorize symptom text with TF-IDF
4. Extract clinical features
5. Train Random Forest classifier
6. Calculate biochemical profiles
7. Save artifacts to `artifacts/`

**Output**:
- `artifacts/waterborne_disease_model.pkl`
- `artifacts/waterborne_artifacts.pkl`

### Generating Symptom Data
```bash
python scripts/generate_symptom_data.py
```

**Output**: `data/reference/symptom_data.csv`

### Training Alternative Models
```bash
python scripts/train_symptom_model.py
```

## Data Pipeline

```
data/training/waterborne_disease_data.csv
                    ↓
            scripts/train_waterborne_model.py
                    ↓
            Feature Engineering & Encoding
                    ↓
            TF-IDF Vectorization + Clinical Features
                    ↓
            Random Forest Classifier Training
                    ↓
            Biochemical Profile Calculation
                    ↓
            artifacts/waterborne_artifacts.pkl
                    ↓
            Backend Application (utils.py)
                    ↓
            Prediction API
```

## File Sizes Reference

| Component | File | Size | Purpose |
|-----------|------|------|---------|
| Training Data | waterborne_disease_data.csv | ~20 KB | Model training |
| Reference Data | symptom_data.csv | ~15 KB | Reference |
| Reference Data | data.csv | ~50 KB | Validation |
| Artifacts | waterborne_artifacts.pkl | ~3 MB | Complete model |
| Model | waterborne_disease_model.pkl | ~2 MB | Classifier only |
| Notebook | MLnote.ipynb | ~500 KB | Analysis |

## Best Practices

### Data Management
1. Keep training data in `data/training/`
2. Maintain reference data in `data/reference/`
3. Never modify original CSV files; create copies for experiments
4. Version your datasets (e.g., `waterborne_disease_data_v2.csv`)

### Model Management
1. Save all trained models to `artifacts/`
2. Include training date in model names
3. Keep detailed notes on model performance
4. Archive old models with version numbers

### Script Organization
1. Keep training scripts in `scripts/`
2. Add docstrings to all functions
3. Configure paths at script top
4. Use logging for debugging

### Notebook Organization
1. Document analysis in `notebooks/`
2. Include data source references
3. Clean up before committing
4. Add markdown explanations

## Integration with Backend

**Model Loading** (in `backend/Health_Monitoring_System/web/utils.py`):
```python
WATERBORNE_ARTIFACTS_PATH = r'c:\PY26112\source\ml-models\artifacts\waterborne_artifacts.pkl'

def load_artifacts():
    with open(WATERBORNE_ARTIFACTS_PATH, 'rb') as f:
        artifacts = pickle.load(f)
    return artifacts
```

**Prediction Pipeline**:
```
User Input → Text Vectorization → Feature Extraction → Model Prediction → Disease → Remedy
```

## Maintenance & Updates

### Adding New Data
1. Save to `data/training/` or `data/reference/`
2. Document in this README
3. Update training script if needed
4. Retrain model and update artifacts

### Updating Model
1. Modify training script
2. Run training (recommended: create experiment branch)
3. Evaluate new model
4. Replace artifacts if improved
5. Test with backend application

### Archiving Old Files
1. Create `archived/` subdirectory if needed
2. Move outdated models and data
3. Document archive contents
4. Keep reference for version history

## Next Steps

1. **Expand Dataset**: Add more real-world data to `data/training/`
2. **Improve Model**: Experiment with new algorithms in `scripts/`
3. **Add Diseases**: Extend model to predict 20+ diseases
4. **Production Deployment**: Use versioned artifacts for production

---

**Last Updated**: February 6, 2026  
**Version**: 1.0  
**Status**: Professionally Organized ✅
