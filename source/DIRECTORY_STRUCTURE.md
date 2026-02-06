# Complete Project Directory Structure - Professional Organization

## Executive Overview

This document provides a comprehensive visual and detailed breakdown of the entire Waterborne Disease Health Monitoring System directory structure, with emphasis on professional organization and file management.

---

## Main Directory Tree

```
PY26112/                                    # PROJECT ROOT
│
├── source/                                 # MAIN SOURCE DIRECTORY (PRODUCTION)
│   │
│   ├── backend/                            # DJANGO WEB APPLICATION
│   │   ├── Health_Monitoring_System/       # Django project package
│   │   │   ├── __init__.py
│   │   │   ├── asgi.py                    # ASGI configuration
│   │   │   ├── wsgi.py                    # WSGI configuration
│   │   │   ├── settings.py                # Project settings (SECRET_KEY, DB, apps)
│   │   │   └── urls.py                    # Project URL routing
│   │   │
│   │   ├── web/                           # Main Django application
│   │   │   ├── __init__.py
│   │   │   ├── admin.py                   # Django admin configuration
│   │   │   ├── apps.py                    # App configuration
│   │   │   ├── forms.py                   # User signup form
│   │   │   ├── models.py                  # DiseaseInfo model
│   │   │   ├── tests.py                   # Unit tests
│   │   │   ├── urls.py                    # App-level URL routing
│   │   │   ├── utils.py                   # ML prediction integration
│   │   │   ├── views.py                   # View functions (home, signup, predict)
│   │   │   │
│   │   │   ├── management/                # Management commands
│   │   │   │   └── commands/
│   │   │   │       ├── __init__.py
│   │   │   │       └── populate_waterborne_diseases.py  # DB population
│   │   │   │
│   │   │   ├── migrations/                # Database migrations
│   │   │   │   ├── __init__.py
│   │   │   │   └── 0001_initial.py
│   │   │   │
│   │   │   ├── static/                    # Static files (CSS, JS, images)
│   │   │   │   └── web/
│   │   │   │       └── css/
│   │   │   │           └── styles.css     # Main stylesheet
│   │   │   │
│   │   │   └── templates/                 # HTML templates
│   │   │       └── web/
│   │   │           ├── base.html          # Base layout template
│   │   │           ├── home.html          # Dashboard/home page
│   │   │           ├── login.html         # Login page
│   │   │           ├── predict.html       # Prediction interface
│   │   │           └── signup.html        # User registration
│   │   │
│   │   ├── manage.py                      # Django management utility
│   │   ├── db.sqlite3                     # SQLite database (development)
│   │   └── requirements.txt               # Python dependencies
│   │
│   ├── ml-models/                         # MACHINE LEARNING COMPONENTS (PROFESSIONALLY ORGANIZED)
│   │   │
│   │   ├── data/                          # DATA MANAGEMENT
│   │   │   ├── training/                  # Training datasets
│   │   │   │   └── waterborne_disease_data.csv
│   │   │   │       ├── 54 samples
│   │   │   │       ├── 6 disease classes
│   │   │   │       ├── 19 features
│   │   │   │       └── Format: CSV with headers
│   │   │   │
│   │   │   └── reference/                 # Reference and validation data
│   │   │       ├── symptom_data.csv       # Symptom reference dataset
│   │   │       └── data.csv               # General reference dataset
│   │   │
│   │   ├── artifacts/                     # TRAINED MODELS & SERIALIZED OBJECTS
│   │   │   ├── waterborne_artifacts.pkl
│   │   │   │   ├── Complete model pipeline
│   │   │   │   ├── Random Forest classifier
│   │   │   │   ├── TF-IDF vectorizer
│   │   │   │   ├── Label encoders
│   │   │   │   └── Biochemical profiles
│   │   │   │
│   │   │   ├── waterborne_disease_model.pkl
│   │   │   │   ├── Standalone RF classifier
│   │   │   │   ├── 150 estimators
│   │   │   │   └── 72.73% test accuracy
│   │   │   │
│   │   │   ├── simplified_model_artifacts.pkl
│   │   │   ├── symptom_model.pkl
│   │   │   └── water_disease_model.pkl
│   │   │
│   │   ├── scripts/                       # TRAINING & DATA PROCESSING SCRIPTS
│   │   │   ├── train_waterborne_model.py
│   │   │   │   ├── Main training script
│   │   │   │   ├── Feature engineering
│   │   │   │   ├── Model training
│   │   │   │   └── Artifact serialization
│   │   │   │
│   │   │   ├── generate_symptom_data.py
│   │   │   │   └── Synthetic data generation
│   │   │   │
│   │   │   └── train_symptom_model.py
│   │   │       └── Alternative model training
│   │   │
│   │   ├── notebooks/                     # JUPYTER NOTEBOOKS
│   │   │   └── MLnote.ipynb
│   │   │       ├── Exploratory analysis
│   │   │       ├── Feature visualization
│   │   │       └── Model documentation
│   │   │
│   │   ├── models/                        # FUTURE: Multiple model storage
│   │   │   └── [Reserved for versioned models]
│   │   │
│   │   └── DIRECTORY_STRUCTURE.md         # ML-models documentation
│   │
│   ├── docs/                              # COMPREHENSIVE DOCUMENTATION
│   │   ├── README.md                      # Project overview
│   │   ├── INSTALLATION.md                # Setup and installation
│   │   ├── API.md                         # API endpoint documentation
│   │   ├── USER_GUIDE.md                  # End-user manual
│   │   ├── ML_MODEL.md                    # Model architecture details
│   │   ├── DATABASE_SCHEMA.md             # Database design
│   │   └── [Additional guides]
│   │
│   ├── ROOT DOCUMENTATION & CONFIGURATION
│   │   ├── README.md                      # Main project README
│   │   ├── MANIFEST.md                    # File manifest
│   │   ├── PROJECT_SUMMARY.md             # Complete project summary
│   │   ├── COMPLETION_REPORT.md           # Delivery report
│   │   ├── DIRECTORY_STRUCTURE.md         # This file
│   │   ├── requirements.txt               # All dependencies
│   │   ├── SOURCE_INDEX.json              # Component index
│   │   ├── FILE_INVENTORY.md              # File listing
│   │   └── organize_source.py             # Organization script
│   │
│   └── [All above files organized at root]
│
├── Backend/                                # LEGACY SOURCE (REFERENCE)
│   ├── train_simplified.py
│   ├── train_waterborne_model.py
│   │
│   ├── Health_Monitoring_System/
│   │   ├── manage.py
│   │   ├── populate_db.py
│   │   ├── [Django structure]
│   │   └── [Copied to source/backend/]
│   │
│   └── MLnotebooks/
│       ├── [Original ML files]
│       ├── [Data files]
│       └── [Model files]
│
└── README.md                              # Root project README
```

---

## Directory Organization Levels

### Level 0: Project Root (`PY26112/`)
```
Purpose: Top-level project container
Contains: source/ directory and legacy Backend/ reference
```

### Level 1: Source Directory (`source/`)
```
Purpose: Production-ready organized source code
Subdirectories:
  - backend/     (Django application)
  - ml-models/   (ML components)
  - docs/        (Documentation)
```

### Level 2: Backend (`source/backend/`)
```
Purpose: Web application and database
Structure:
  - Django project (Health_Monitoring_System/)
  - Django app (web/)
  - Database (db.sqlite3)
  - Dependencies (requirements.txt)
  - Management (manage.py)
```

### Level 2: ML Models (`source/ml-models/`)
```
Purpose: Machine learning pipeline (professionally organized)
Structure:
  - data/        (Training and reference datasets)
  - artifacts/   (Trained models and serialized objects)
  - scripts/     (Training and processing scripts)
  - notebooks/   (Analysis and documentation)
  - models/      (Future: versioned models)
```

### Level 2: Documentation (`source/docs/`)
```
Purpose: Comprehensive project documentation
Contents:
  - Setup guides
  - API references
  - User manuals
  - Technical specifications
```

---

## Professional Organization Standards Applied

### 1. Data Management (`data/` directory)
✅ **Standard**: Separate training and reference data
✅ **Structure**: 
  - `training/` - Active training datasets
  - `reference/` - Reference and validation data
✅ **Benefits**:
  - Clear separation of concerns
  - Easy data versioning
  - Prevents accidental modification of original data

### 2. Model Artifacts (`artifacts/` directory)
✅ **Standard**: Centralized serialized models
✅ **Structure**: All `.pkl` files in one location
✅ **Benefits**:
  - Single source of truth for models
  - Easy backup and deployment
  - Clear model versioning

### 3. Scripts (`scripts/` directory)
✅ **Standard**: Organized training and processing scripts
✅ **Structure**: Modular Python scripts
✅ **Benefits**:
  - Reproducible model training
  - Easy to track experiments
  - Maintainable code organization

### 4. Notebooks (`notebooks/` directory)
✅ **Standard**: Jupyter notebooks for analysis
✅ **Structure**: Exploratory and documentation notebooks
✅ **Benefits**:
  - Interactive analysis and visualization
  - Documentation with code
  - Easy to share findings

### 5. Backend Application
✅ **Standard**: Django best practices
✅ **Structure**: Follows Django conventions
✅ **Benefits**:
  - Scalable web framework
  - Built-in security
  - Easy maintenance

### 6. Documentation
✅ **Standard**: Comprehensive markdown documentation
✅ **Structure**: Organized by topic
✅ **Benefits**:
  - Versioned with code
  - Easy to search
  - Multiple audience levels

---

## File Organization by Category

### Data Files (CSV)
```
Location: source/ml-models/data/
├── training/
│   └── waterborne_disease_data.csv      (54 samples, 19 features)
└── reference/
    ├── symptom_data.csv                 (Reference dataset)
    └── data.csv                         (Validation dataset)
```

### Model Files (PKL)
```
Location: source/ml-models/artifacts/
├── waterborne_artifacts.pkl             (3 MB, complete pipeline)
├── waterborne_disease_model.pkl         (2 MB, classifier)
├── simplified_model_artifacts.pkl       (Lightweight version)
├── symptom_model.pkl                    (Legacy model)
└── water_disease_model.pkl              (Alternative model)
```

### Script Files (PY)
```
Location: source/ml-models/scripts/
├── train_waterborne_model.py            (Main training script)
├── generate_symptom_data.py             (Data generation)
└── train_symptom_model.py               (Alternative training)
```

### Database Files (DB)
```
Location: source/backend/
└── db.sqlite3                           (5 MB, SQLite database)
    ├── auth_user table
    └── web_diseaseinfo table
```

### Template Files (HTML)
```
Location: source/backend/web/templates/web/
├── base.html                            (Base layout)
├── home.html                            (Dashboard)
├── login.html                           (Authentication)
├── predict.html                         (Prediction interface)
└── signup.html                          (Registration)
```

### Style Files (CSS)
```
Location: source/backend/web/static/web/css/
└── styles.css                           (Main stylesheet)
```

### Configuration Files
```
Location: source/
├── requirements.txt                     (Python dependencies)
├── SOURCE_INDEX.json                    (Component index)
├── README.md                            (Overview)
├── MANIFEST.md                          (File manifest)
├── PROJECT_SUMMARY.md                   (Summary)
└── COMPLETION_REPORT.md                 (Delivery report)

Location: source/ml-models/
└── DIRECTORY_STRUCTURE.md               (ML organization)

Location: source/backend/
└── requirements.txt                     (Backend dependencies)
```

---

## File Count Summary

| Category | Location | Count | Type |
|----------|----------|-------|------|
| **Source Code** | source/ | 50+ | Python, HTML, CSS |
| **Data Files** | ml-models/data/ | 3 | CSV |
| **Models** | ml-models/artifacts/ | 5 | PKL |
| **Scripts** | ml-models/scripts/ | 3 | Python |
| **Notebooks** | ml-models/notebooks/ | 1 | Jupyter |
| **Documentation** | ml-models/, docs/, source/ | 10 | Markdown |
| **Database** | backend/ | 1 | SQLite |
| **Configuration** | Various | 5 | TXT, JSON |
| **Total** | **source/** | **78+** | **Multiple** |

---

## Integration Architecture

```
┌────────────────────────────────────────────────────────┐
│            USER INTERFACE (Browser)                     │
│              source/backend/templates/                 │
└────────────────┬─────────────────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│        DJANGO WEB APPLICATION                          │
│        source/backend/web/views.py                    │
│        source/backend/web/forms.py                    │
│        source/backend/web/urls.py                     │
└────────────────┬─────────────────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│        ML PREDICTION ENGINE                            │
│        source/backend/web/utils.py                    │
│                   │                                     │
│                   ▼                                     │
│        Load Artifacts:                                 │
│        ml-models/artifacts/waterborne_artifacts.pkl   │
└────────────────┬─────────────────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│        DATABASE (Disease & User Data)                  │
│        source/backend/db.sqlite3                       │
│        ├─ auth_user                                    │
│        └─ web_diseaseinfo                             │
└────────────────────────────────────────────────────────┘
```

---

## Data Flow Through Directory Structure

### Prediction Pipeline
```
1. User Input (template: predict.html)
           ↓
2. Django View (views.py)
           ↓
3. ML Prediction (utils.py)
           ↓
4. Load Model (artifacts/waterborne_artifacts.pkl)
           ↓
5. TF-IDF Processing (text vectorization)
           ↓
6. Feature Engineering (age, gender, water source)
           ↓
7. Random Forest Classification
           ↓
8. Result Display (predict.html)
           ↓
9. Database Lookup (db.sqlite3 → remedy, profile)
           ↓
10. Response to User
```

### Model Training Pipeline
```
1. Input Data (data/training/waterborne_disease_data.csv)
           ↓
2. Training Script (scripts/train_waterborne_model.py)
           ↓
3. Data Preprocessing
           ↓
4. Feature Engineering
           ↓
5. TF-IDF Vectorization
           ↓
6. Model Training (Random Forest)
           ↓
7. Model Evaluation
           ↓
8. Artifact Serialization
           ↓
9. Save Models (artifacts/*.pkl)
```

---

## Best Practices Implemented

### ✅ Separation of Concerns
- Data separate from code
- Models separate from training
- Frontend separate from backend
- Configuration separate from code

### ✅ Scalability
- Modular directory structure
- Easy to add new models
- Easy to add new datasets
- Easy to extend functionality

### ✅ Maintainability
- Clear naming conventions
- Organized file structure
- Comprehensive documentation
- Version control ready

### ✅ Security
- Database in dedicated location
- Secrets in configuration
- Source code isolated
- Models in protected artifacts

### ✅ Accessibility
- Multiple documentation levels
- Clear directory structure
- Easy file discovery
- Intuitive organization

---

## Customization Guide

### Adding New Dataset
```
1. Place training data in: source/ml-models/data/training/
2. Place reference data in: source/ml-models/data/reference/
3. Update DIRECTORY_STRUCTURE.md
4. Retrain model using scripts/
```

### Adding New Model
```
1. Create training script in: source/ml-models/scripts/
2. Train and save to: source/ml-models/artifacts/
3. Update utils.py to load new model
4. Test with backend application
```

### Adding New Notebook
```
1. Place in: source/ml-models/notebooks/
2. Document analysis and findings
3. Reference data files and models
```

### Adding New Disease
```
1. Add data to: source/ml-models/data/
2. Retrain model
3. Run: python manage.py populate_waterborne_diseases
4. Verify in web interface
```

---

## Directory Maintenance Checklist

- [ ] All CSV files in `ml-models/data/`
- [ ] All models in `ml-models/artifacts/`
- [ ] All scripts in `ml-models/scripts/`
- [ ] All notebooks in `ml-models/notebooks/`
- [ ] Backend code in `backend/`
- [ ] Documentation in `docs/`
- [ ] No duplicate files in multiple locations
- [ ] All dependencies in `requirements.txt`
- [ ] Database backed up regularly
- [ ] Models versioned appropriately

---

## Version Control Recommendations

```
.gitignore should exclude:
- __pycache__/
- *.pyc
- db.sqlite3
- venv/
- .env
- *.log

Should include:
- All source code
- Data files (CSV)
- Configuration files
- Documentation
- Scripts
```

---

## Production Deployment Checklist

- [ ] Update SECRET_KEY in settings.py
- [ ] Set DEBUG = False
- [ ] Configure PostgreSQL database
- [ ] Move SQLite backup to archives
- [ ] Verify all models in artifacts/
- [ ] Update paths for production server
- [ ] Enable HTTPS/SSL
- [ ] Setup logging
- [ ] Configure backups
- [ ] Test prediction pipeline

---

**Directory Structure Version**: 1.0  
**Last Updated**: February 6, 2026  
**Status**: ✅ Professionally Organized  
**Organization Standard**: Enterprise-Ready
