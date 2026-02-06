# Waterborne Disease Monitoring System - Source Code Manifest

## Backend Components

### Django Project Structure
```
backend/
├── Health_Monitoring_System/          # Main project package
│   ├── __init__.py
│   ├── asgi.py                       # ASGI configuration
│   ├── wsgi.py                       # WSGI configuration
│   ├── settings.py                   # Project settings
│   └── urls.py                       # Project URL routing
├── web/                              # Main Django app
│   ├── __init__.py
│   ├── admin.py                      # Django admin configuration
│   ├── apps.py                       # App configuration
│   ├── forms.py                      # Django forms (SignupForm)
│   ├── models.py                     # Database models (DiseaseInfo)
│   ├── tests.py                      # Unit tests
│   ├── urls.py                       # App URL routing
│   ├── utils.py                      # ML prediction utilities
│   ├── views.py                      # View functions (home, signup, predict)
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── populate_waterborne_diseases.py  # DB population command
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py          # Initial migrations
│   ├── static/
│   │   └── web/
│   │       └── css/
│   │           └── styles.css        # Frontend styling
│   └── templates/
│       └── web/
│           ├── base.html             # Base template
│           ├── home.html             # Home page
│           ├── login.html            # Login page
│           ├── predict.html          # Prediction page
│           └── signup.html           # Signup page
└── manage.py                         # Django management utility
```

## Machine Learning Components

### Training & Models
```
ml-models/
├── waterborne_disease_data.csv       # Training dataset (54 samples)
├── train_waterborne_model.py         # Training script
├── waterborne_disease_model.pkl      # Trained RandomForest model
├── waterborne_artifacts.pkl          # Complete artifacts package
└── MLnote.ipynb                      # Analysis notebook
```

### Dataset Description
- **Rows**: 54 samples
- **Features**: 19 columns
  - Clinical: Age, Gender, Water_Source, Hygiene_Score
  - Symptoms: Symptom_Text
  - Water Quality: Water_Color, Water_Odor
  - Biochemical: Sodium, Potassium, Chloride, WBC, Hemoglobin, Platelets, etc.
- **Target**: 6 disease classes
  - Cholera
  - Typhoid
  - Hepatitis A
  - Dysentery
  - Giardiasis
  - E. coli Infection

### Model Specifications
- **Algorithm**: Random Forest Classifier (150 estimators)
- **Text Processing**: TF-IDF Vectorizer (max 100 features, bi-grams)
- **Clinical Features**: 6 numerical features
- **Combined Features**: 106 total (100 TF-IDF + 6 clinical)
- **Training Accuracy**: 100%
- **Testing Accuracy**: 72.73%

## Key Files Description

### models.py
```python
class DiseaseInfo(models.Model):
    name = CharField(max_length=100, unique=True)
    remedy = TextField()
    bio_profile = TextField()  # JSON string
```

### utils.py
Main function: `make_prediction(data_dict)`
- Loads trained artifacts
- Processes symptom text with TF-IDF
- Encodes categorical features
- Makes disease prediction
- Retrieves remedy and biochemical profile

### views.py
- `home()` - Home page view (login required)
- `signup()` - User registration
- `predict_water_quality()` - Main prediction endpoint

### train_waterborne_model.py
Training pipeline:
1. Load waterborne disease dataset
2. Encode categorical features
3. Vectorize symptom text
4. Extract clinical features
5. Train Random Forest model
6. Calculate biochemical profiles
7. Save artifacts

## System Dependencies

```
Django==5.0.0
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.24.3
scipy==1.11.4
```

## Data Flow

1. **User Input** → Web Form
   - Symptom_Text (free text)
   - Water_Color (Clear/Turbid)
   - Water_Odor (None/Fishy/Musty)
   - Optional: Age, Gender, Water_Source, Hygiene_Score

2. **Processing** → Prediction Engine
   - TF-IDF vectorization of symptoms
   - Categorical encoding
   - Feature combination

3. **Prediction** → Model
   - Random Forest classification
   - Disease prediction
   - Confidence estimation

4. **Results** → Database Lookup
   - DiseaseInfo retrieval
   - Remedy recommendation
   - Biochemical profile display

5. **Output** → User View
   - Disease name
   - Treatment recommendations
   - Normal biochemical values
   - Clinical guidance

## Frontend Components

### Templates
- **base.html** - Base layout with CSS
- **home.html** - Dashboard/home screen
- **login.html** - User login interface
- **signup.html** - User registration interface
- **predict.html** - Disease prediction interface

### Styling
- **styles.css** - Main stylesheet for responsive design

## Authentication

- User registration via SignupForm
- Django default user authentication
- Login required for prediction access
- Password validation and hashing

## Database

- **Default**: SQLite3
- **Migrations**: Auto-generated from models
- **Initial Data**: Populated via management command
- **Tables**: 
  - auth_user (Django default)
  - web_diseaseinfo (Custom)
  - Django admin tables

## Deployment Considerations

1. Update `SECRET_KEY` in settings.py
2. Set `DEBUG = False` for production
3. Configure allowed hosts
4. Use environment variables for sensitive data
5. Set up proper logging
6. Configure email for alerts
7. Use production-grade database (PostgreSQL)
8. Set up HTTPS/SSL
9. Configure CORS headers
10. Implement rate limiting

## Testing

Unit tests in `web/tests.py`:
- Model tests
- View tests
- Form validation tests
- Prediction accuracy tests

Run tests:
```bash
python manage.py test
```

## Monitoring & Logging

Add to settings.py:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'health_monitoring.log',
        },
    },
}
```

## Documentation Files Location

- API documentation: `/docs/API.md`
- Installation guide: `/docs/INSTALLATION.md`
- User manual: `/docs/USER_GUIDE.md`
- ML documentation: `/docs/ML_MODEL.md`

---

**Version**: 1.0
**Last Updated**: February 6, 2026
**Python Version**: 3.13.7
**Django Version**: 5.0+
