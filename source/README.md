# Waterborne Disease Health Monitoring System - Source Files

This directory contains all backend, frontend, ML model, and related source files for **AquaHealth**, a Smart Community Health Monitoring and Early Warning System focused on waterborne disease prediction, **professionally organized with centralized data management**.

## 📁 Directory Structure (Professionally Organized)

### `/backend`
Contains all Django web application code including:
- Django project configuration (Health_Monitoring_System/)
- Web application code (web/)
- Database models and forms (DiseaseInfo, User)
- Views, URLs, and utilities with ML integration
- HTML templates and static files (CSS, JS)
- Management commands for database population
- SQLite database (db.sqlite3) with 6 diseases populated

### `/ml-models` (Professional Data Organization)
Machine learning pipeline with organized data management:

**`data/`** - Centralized data management
- `training/` - Training datasets
  - `waterborne_disease_data.csv` (54 samples, 6 classes, 19 features)
- `reference/` - Reference and validation data
  - `symptom_data.csv` (symptom reference)
  - `data.csv` (general reference)

**`artifacts/`** - Trained models and serialized objects
- `waterborne_artifacts.pkl` (Complete pipeline with encoders)
- `waterborne_disease_model.pkl` (Standalone classifier)
- Additional model variants for comparison

**`scripts/`** - Training and processing scripts
- `train_waterborne_model.py` (Main training pipeline)
- `generate_symptom_data.py` (Data generation)
- `train_symptom_model.py` (Alternative training)

**`notebooks/`** - Jupyter notebooks for analysis
- `MLnote.ipynb` (Exploratory analysis and documentation)

**`models/`** - Reserved for versioned models

### `/docs`
Comprehensive documentation files:
- README.md - Project overview
- INSTALLATION.md - Step-by-step setup
- API.md - API endpoint documentation
- USER_GUIDE.md - End-user manual with disease profiles
- ML_MODEL.md - Model architecture and training details
- DATABASE_SCHEMA.md - Database design and queries
- PROJECT_SUMMARY.md - Complete technical overview

## Setup Instructions

### Prerequisites
- Python 3.13+
- Django
- scikit-learn
- pandas
- numpy
- scipy

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend/Health_Monitoring_System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Populate waterborne diseases database:
   ```bash
   python manage.py populate_waterborne_diseases
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Features

- **Real-time Disease Prediction**: Uses ML model to predict waterborne diseases based on symptoms and water quality indicators
- **Database of Diseases**: Comprehensive information about waterborne diseases including remedies and biochemical profiles
- **User Authentication**: Secure login and signup system
- **Symptom-based Prediction**: Text-based symptom input with TF-IDF vectorization
- **Water Quality Assessment**: Integration of water color, odor, and source quality indicators
- **Biochemical Profiling**: Display of typical biochemical values for predicted diseases

## Key Models

1. **Cholera** - Severe watery diarrhea and dehydration
2. **Typhoid** - Sustained fever with systemic symptoms
3. **Hepatitis A** - Hepatitis with jaundice and elevated liver enzymes
4. **Dysentery** - Bloody diarrhea with abdominal cramping
5. **Giardiasis** - Parasitic infection causing greasy diarrhea
6. **E. coli Infection** - Enteroinvasive disease with various presentations

## Project Files Overview

### Backend Architecture
- `manage.py` - Django management utility
- `Health_Monitoring_System/settings.py` - Project configuration
- `Health_Monitoring_System/urls.py` - URL routing
- `web/models.py` - Database models (DiseaseInfo)
- `web/views.py` - View logic for prediction and authentication
- `web/utils.py` - Machine learning prediction utilities
- `web/forms.py` - Django forms for user input
- `web/urls.py` - App-level URL routing
- `web/templates/` - HTML templates for web interface

### ML Training Pipeline
- `waterborne_disease_data.csv` - Training dataset with 54 samples
- `train_waterborne_model.py` - Model training script
  - Uses TF-IDF for symptom text vectorization
  - Combines with clinical features (age, gender, water source, hygiene score)
  - Random Forest classifier for disease prediction
  - Calculates biochemical profiles per disease

### Artifacts
- `waterborne_artifacts.pkl` - Serialized model components including:
  - Trained RandomForest model
  - TF-IDF vectorizer
  - Label encoders for categorical features
  - Biochemical profiles per disease

## Model Performance

- Training accuracy: 100%
- Testing accuracy: 72.73%
- 6 disease classes
- 106 combined features (100 TF-IDF + 6 clinical features)

## API Endpoints

- `POST /predict` - Prediction endpoint
  - Required parameters: Symptom_Text, Water_Color, Water_Odor
  - Optional parameters: Age, Gender, Water_Source, Hygiene_Score
  - Returns: Disease prediction, remedy, and biochemical profile

- `GET /home` - Home page
- `POST /signup` - User registration
- `GET/POST /login` - User authentication

## Database Schema

### DiseaseInfo Model
- `name` (CharField) - Disease name
- `remedy` (TextField) - Treatment recommendations
- `bio_profile` (TextField) - JSON string of biochemical values

## Technologies Used

- **Backend**: Django 5.0+
- **ML Framework**: scikit-learn
- **Data Processing**: pandas, numpy
- **NLP**: TF-IDF Vectorizer
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3

## Future Enhancements

1. Deep learning models (LSTM for time-series prediction)
2. Real-time water quality monitoring integration
3. Mobile app development
4. SMS/Email alert system
5. Geographic heat maps for outbreak tracking
6. Community reporting system
7. Advanced epidemiological analytics

## License

This project is developed for public health monitoring and disease prevention.

## Contact & Support

For technical support or inquiries, please refer to the project documentation and Django documentation.

---

**Last Updated**: February 6, 2026
**System Version**: 1.0
**Python Version**: 3.13.7
