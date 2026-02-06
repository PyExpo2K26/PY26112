# Professional Directory Tree Visualization

## Complete Source Directory Structure

```
source/
│
├── 📄 README.md                           # Main project overview
├── 📄 MANIFEST.md                         # File manifest and catalog
├── 📄 DIRECTORY_STRUCTURE.md              # Professional organization guide
├── 📄 PROJECT_SUMMARY.md                  # Complete project summary
├── 📄 COMPLETION_REPORT.md                # Delivery and completion report
├── 📄 requirements.txt                    # Global Python dependencies
├── 📄 SOURCE_INDEX.json                   # Component index (JSON)
├── 📄 FILE_INVENTORY.md                   # Complete file inventory
├── 📄 organize_source.py                  # Source organization script
│
│
├── 📁 backend/                            ← DJANGO WEB APPLICATION
│   ├── 📁 Health_Monitoring_System/       # Django project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── wsgi.py
│   │   ├── settings.py                    # Configuration
│   │   └── urls.py                        # URL routing
│   │
│   ├── 📁 web/                            # Django app
│   │   ├── 📁 management/
│   │   │   └── commands/
│   │   │       ├── __init__.py
│   │   │       └── populate_waterborne_diseases.py  # DB population
│   │   │
│   │   ├── 📁 migrations/
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   │
│   │   ├── 📁 static/
│   │   │   └── web/
│   │   │       └── css/
│   │   │           └── styles.css         # ★ Styling
│   │   │
│   │   ├── 📁 templates/
│   │   │   └── web/
│   │   │       ├── base.html              # ★ Base layout
│   │   │       ├── home.html              # ★ Dashboard
│   │   │       ├── login.html             # ★ Login
│   │   │       ├── predict.html           # ★ Prediction interface
│   │   │       └── signup.html            # ★ Registration
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py                       # Admin configuration
│   │   ├── apps.py                        # App config
│   │   ├── forms.py                       # User form (SignupForm)
│   │   ├── models.py                      # ★ DiseaseInfo model
│   │   ├── tests.py                       # Unit tests
│   │   ├── urls.py                        # App routing
│   │   ├── utils.py                       # ★ ML prediction integration
│   │   └── views.py                       # ★ View logic
│   │
│   ├── 📄 manage.py                       # Django CLI
│   ├── 📄 db.sqlite3                      # ★ SQLite database (5 MB)
│   │                                       #   - 6 diseases populated
│   │                                       #   - User authentication
│   │                                       #   - Prediction history
│   └── 📄 requirements.txt                # Backend dependencies
│
│
├── 📁 ml-models/                          ← MACHINE LEARNING (PROFESSIONALLY ORGANIZED)
│   ├── 📁 data/                           # ★ CENTRALIZED DATA MANAGEMENT
│   │   │
│   │   ├── 📁 training/                   # Training datasets
│   │   │   └── 📊 waterborne_disease_data.csv
│   │   │       ├─ 54 samples
│   │   │       ├─ 6 disease classes (balanced)
│   │   │       ├─ 19 features (clinical, biochemical, symptoms)
│   │   │       └─ Format: CSV with headers
│   │   │
│   │   └── 📁 reference/                  # Reference & validation data
│   │       ├── 📊 symptom_data.csv        # Symptom reference dataset
│   │       └── 📊 data.csv                # General reference dataset
│   │
│   ├── 📁 artifacts/                      # ★ TRAINED MODELS
│   │   ├── 📦 waterborne_artifacts.pkl    # Complete ML pipeline
│   │   │   ├─ Random Forest classifier
│   │   │   ├─ TF-IDF vectorizer
│   │   │   ├─ Label encoders (5 types)
│   │   │   └─ Biochemical profiles
│   │   │
│   │   ├── 📦 waterborne_disease_model.pkl # Standalone classifier
│   │   │   ├─ 150 tree estimators
│   │   │   └─ 72.73% test accuracy
│   │   │
│   │   ├── 📦 simplified_model_artifacts.pkl
│   │   ├── 📦 symptom_model.pkl           # Legacy model
│   │   └── 📦 water_disease_model.pkl     # Alternative model
│   │
│   ├── 📁 scripts/                        # ★ TRAINING SCRIPTS
│   │   ├── 🐍 train_waterborne_model.py
│   │   │   ├─ Data preprocessing
│   │   │   ├─ Feature engineering
│   │   │   ├─ TF-IDF vectorization
│   │   │   ├─ Model training
│   │   │   └─ Artifact serialization
│   │   │
│   │   ├── 🐍 generate_symptom_data.py
│   │   │   └─ Synthetic data generation
│   │   │
│   │   └── 🐍 train_symptom_model.py
│   │       └─ Alternative training pipeline
│   │
│   ├── 📁 notebooks/                      # Jupyter notebooks
│   │   └── 📓 MLnote.ipynb
│   │       ├─ Exploratory data analysis
│   │       ├─ Feature visualization
│   │       └─ Model documentation
│   │
│   ├── 📁 models/                         # Reserved for versioned models
│   │   └── [Future: model_v1_production/]
│   │
│   └── 📄 DIRECTORY_STRUCTURE.md          # ML-models detailed documentation
│
│
├── 📁 docs/                               ← COMPREHENSIVE DOCUMENTATION
│   ├── 📄 README.md                       # Project overview
│   ├── 📄 INSTALLATION.md                 # 📌 Setup guide (detailed)
│   ├── 📄 API.md                          # 📌 API documentation (endpoint reference)
│   ├── 📄 USER_GUIDE.md                   # 📌 User manual (disease profiles, FAQ)
│   ├── 📄 ML_MODEL.md                     # 📌 Model documentation (architecture, training)
│   ├── 📄 DATABASE_SCHEMA.md              # 📌 Database design (schema, queries)
│   └── 📄 PROJECT_SUMMARY.md              # 📌 Technical overview
│
└── 📄 [Configuration Files Root]
    ├── requirements.txt                   # All dependencies
    ├── SOURCE_INDEX.json                  # Component index
    └── FILE_INVENTORY.md                  # File listing


═══════════════════════════════════════════════════════════════════

SYMBOL REFERENCE:
├──  Folder/file structure
├─   Property/feature
└─   Last item
📁  Directory folder
📄  Documentation file
🐍  Python script
📦  Serialized model (pickle)
📊  Data file (CSV)
📓  Jupyter notebook
★    Important/frequently used
│    Vertical line continuation

═══════════════════════════════════════════════════════════════════
```

---

## Data Organization Summary

### 🎯 CSV Files Organization

**Location**: `ml-models/data/`

```
data/
├── training/
│   └── waterborne_disease_data.csv         ← MAIN TRAINING DATA
│       Purpose: Train the ML model
│       Size: 54 samples × 19 features
│       Classes: 6 waterborne diseases
│       
├── reference/
│   ├── symptom_data.csv                    ← SUPPLEMENTARY DATA
│   │   Purpose: Alternative symptom reference
│   │   Usage: Data generation, validation
│   │   
│   └── data.csv                            ← REFERENCE DATA
│       Purpose: Model validation
│       Usage: Testing, comparison
```

### 🎯 Model Files Organization

**Location**: `ml-models/artifacts/`

```
artifacts/
├── waterborne_artifacts.pkl (3 MB)         ← PRIMARY MODEL
│   Complete pipeline with all components
│   
├── waterborne_disease_model.pkl (2 MB)     ← CLASSIFIER
│   Standalone model for inference
│   
└── [other model variants]                  ← EXPERIMENTAL
    Reference and alternative models
```

### 🎯 Script Files Organization

**Location**: `ml-models/scripts/`

```
scripts/
├── train_waterborne_model.py               ← MAIN TRAINING
│   Complete training pipeline
│   Reads from: data/training/
│   Writes to: artifacts/
│   
├── generate_symptom_data.py                ← DATA GENERATION
│   Creates synthetic symptoms
│   
└── train_symptom_model.py                  ← ALTERNATIVE
    Alternative model training
```

---

## File Statistics

### by Category

| Category | Count | Location |
|----------|-------|----------|
| **CSV Files** | 3 | `ml-models/data/` |
| **Model Files (PKL)** | 5 | `ml-models/artifacts/` |
| **Python Scripts** | 3 | `ml-models/scripts/` |
| **Jupyter Notebooks** | 1 | `ml-models/notebooks/` |
| **Django App Files** | 15+ | `backend/web/` |
| **HTML Templates** | 5 | `backend/web/templates/` |
| **Configuration Files** | 8 | `source/` root |
| **Documentation Files** | 10 | `docs/` + `ml-models/` |
| **Total** | **50+** | **Organized** |

### by Size

| Component | Size | Type |
|-----------|------|------|
| waterborne_artifacts.pkl | ~3 MB | Model + encoders |
| waterborne_disease_model.pkl | ~2 MB | Classifier |
| db.sqlite3 | ~5 MB | Database |
| MLnote.ipynb | ~500 KB | Notebook |
| CSV files | ~85 KB | Data |
| Python scripts | ~50 KB | Code |
| Documentation | ~200 KB | Markdown |
| **Total** | **~11 MB** | **Compact** |

---

## Quick Navigation

### For Data Scientists
→ Start here: `ml-models/data/` and `ml-models/scripts/`

### For Web Developers
→ Start here: `backend/web/` and `docs/INSTALLATION.md`

### For Users
→ Start here: `docs/USER_GUIDE.md` and access via web browser

### For DevOps
→ Start here: `docs/INSTALLATION.md` and `requirements.txt`

### For Integration
→ Start here: `docs/API.md` and `backend/web/utils.py`

### For Understanding Architecture
→ Start here: `DIRECTORY_STRUCTURE.md` and `docs/ML_MODEL.md`

---

## Professional Organization Standards

✅ **Clear Separation of Concerns**
- Data separate from code
- Models separate from training scripts
- Frontend separate from backend

✅ **Scalability**
- Easy to add new datasets
- Easy to add new models
- Easy to extend functionality

✅ **Maintainability**
- Consistent naming conventions
- Organized directory hierarchy
- Comprehensive documentation

✅ **Reproducibility**
- All training scripts versioned
- All data files tracked
- All models serialized

✅ **Security**
- Database protected
- Secrets in configuration
- Source code isolated

---

**Directory Tree Version**: 1.0  
**Last Updated**: February 6, 2026  
**Organization Status**: ✅ Professional Enterprise-Ready  
**Total Files Organized**: 50+
