"""
Source Organization Script
Organizes and documents all backend, ML, and related source files
for the Waterborne Disease Health Monitoring System
"""

import os
import shutil
import json
from pathlib import Path

# Base directories
PROJECT_ROOT = r'c:\PY26112'
SOURCE_DIR = r'c:\PY26112\source'
BACKEND_DIR = os.path.join(SOURCE_DIR, 'backend')
ML_DIR = os.path.join(SOURCE_DIR, 'ml-models')
DOCS_DIR = os.path.join(SOURCE_DIR, 'docs')

# Source locations
BACKEND_SRC = r'c:\PY26112\Backend\Health_Monitoring_System'
ML_SRC = r'c:\PY26112\Backend\MLnotebooks'
TRAINING_SRC = r'c:\PY26112\Backend\train_waterborne_model.py'

def create_source_index():
    """Create a comprehensive source index file"""
    
    source_index = {
        "project": "Waterborne Disease Health Monitoring System",
        "version": "1.0",
        "created": "2026-02-06",
        "components": {
            "backend": {
                "path": "backend/",
                "description": "Django web application",
                "files": [
                    "Health_Monitoring_System/manage.py",
                    "Health_Monitoring_System/settings.py",
                    "Health_Monitoring_System/urls.py",
                    "Health_Monitoring_System/wsgi.py",
                    "Health_Monitoring_System/asgi.py",
                    "web/models.py",
                    "web/views.py",
                    "web/forms.py",
                    "web/urls.py",
                    "web/utils.py",
                    "web/admin.py",
                    "web/apps.py",
                    "web/management/commands/populate_waterborne_diseases.py",
                    "web/templates/base.html",
                    "web/templates/home.html",
                    "web/templates/login.html",
                    "web/templates/predict.html",
                    "web/templates/signup.html",
                    "web/static/css/styles.css"
                ]
            },
            "ml_models": {
                "path": "ml-models/",
                "description": "Machine learning models and training",
                "files": [
                    "waterborne_disease_data.csv",
                    "train_waterborne_model.py",
                    "waterborne_disease_model.pkl",
                    "waterborne_artifacts.pkl",
                    "MLnote.ipynb",
                    "symptom_data.csv"
                ]
            },
            "documentation": {
                "path": "docs/",
                "description": "Project documentation",
                "files": [
                    "README.md",
                    "API.md",
                    "INSTALLATION.md",
                    "USER_GUIDE.md",
                    "ML_MODEL.md",
                    "DATABASE_SCHEMA.md"
                ]
            }
        },
        "key_features": [
            "Real-time waterborne disease prediction",
            "ML-based classification using Random Forest",
            "TF-IDF text processing for symptoms",
            "Comprehensive biochemical profiling",
            "User authentication and authorization",
            "Web-based prediction interface",
            "Database-driven disease information"
        ],
        "database": {
            "type": "SQLite3",
            "default_location": "db.sqlite3",
            "models": ["DiseaseInfo", "User (Django)"]
        },
        "technologies": [
            "Django 5.0+",
            "scikit-learn 1.3.2",
            "pandas 2.1.3",
            "numpy 1.24.3",
            "scipy 1.11.4",
            "Python 3.13.7"
        ]
    }
    
    index_path = os.path.join(SOURCE_DIR, 'SOURCE_INDEX.json')
    with open(index_path, 'w') as f:
        json.dump(source_index, f, indent=2)
    
    print(f"Created source index: {index_path}")

def list_all_files():
    """List all organized files in source directory"""
    
    file_inventory = {
        "backend": [],
        "ml_models": [],
        "docs": []
    }
    
    # Walk through directories and collect files
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            filepath = os.path.join(root, file)
            relative_path = os.path.relpath(filepath, SOURCE_DIR)
            
            if relative_path.startswith('backend'):
                file_inventory["backend"].append(relative_path)
            elif relative_path.startswith('ml-models'):
                file_inventory["ml_models"].append(relative_path)
            elif relative_path.startswith('docs'):
                file_inventory["docs"].append(relative_path)
    
    # Create file inventory document
    inventory_content = "# Source File Inventory\n\n"
    
    for category, files in file_inventory.items():
        inventory_content += f"## {category.upper().replace('_', ' ')}\n\n"
        for file in sorted(files):
            inventory_content += f"- {file}\n"
        inventory_content += "\n"
    
    inventory_path = os.path.join(SOURCE_DIR, 'FILE_INVENTORY.md')
    with open(inventory_path, 'w') as f:
        f.write(inventory_content)
    
    print(f"Created file inventory: {inventory_path}")

if __name__ == "__main__":
    print("Organizing source files...")
    print(f"Source directory: {SOURCE_DIR}")
    
    create_source_index()
    list_all_files()
    
    print("\nSource organization complete!")
    print("\nDirectory structure:")
    print("""
source/
├── backend/                          # Django web application
├── ml-models/                        # ML models and training
├── docs/                             # Documentation
├── README.md                         # Project overview
├── MANIFEST.md                       # File manifest
├── SOURCE_INDEX.json                 # Component index
└── FILE_INVENTORY.md                 # File listing
    """)
