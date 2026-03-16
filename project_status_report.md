# Water Surveillance Project - Current Status Report

This document details the current architectural and functional level of the **AquaHealth Water Surveillance** project as of its latest codebase updates.

## 1. Overall Architecture
The project is a fully functional **Django-based Web Application** integrated with a **Machine Learning (ML)** risk prediction engine. 
*   **Backend:** Python 3, Django framework
*   **Database:** SQLite3 (Local file-based system)
*   **Machine Learning:** Scikit-Learn (Logistic Regression for scoring, Random Forest for training)
*   **Frontend:** Vanilla HTML, CSS (Custom "Government" styling), and Chart.js for data visualization
*   **Notifications:** Twilio API integration for SMS/WhatsApp alerts

---

## 2. Core Functional Modules

### A. The Machine Learning Risk Engine (`risk_engine.py`)
At the heart of the project is the `RiskEngine` class. It evaluates water quality dynamically:
*   **Contamination Index Calculation:** Computes a strict index based on Turbidity, pH levels, Nitrates, and E.coli presence.
*   **ML Prediction:** Uses a generated `risk_model.pkl` (Logistic Regression) to predict the percentage probability of a health risk based on the input parameters.
*   **Smart Insights Generator:** Automatically generates human-readable strings for the **Likely Cause**, **Potential Effects**, and **Immediate Remedies** when a sample is polluted.

### B. User Role Management (`models.py`)
The system implements a profile extension over the default Django User model, defining hierarchy:
*   **Roles:** `Field Officer` (Default), `District Admin`, and `State Admin`.
*   These are tied directly to submitted samples to track which user reported the data.

### C. Data Collection & Monitoring
*   **`WaterSample` Model:** Stores geographical location (Village, District, Lat/Long), precise water chemistry parameters, and contact information. 
*   **Automated Saving Overrides:** Whenever a `WaterSample` is saved, the ML `RiskEngine` is automatically invoked to generate the Risk Score, calculate remedies, and trigger an Alert if the score exceeds `70`.

### D. Automated Alerting System
*   **`Alert` Model:** Automatically generated for High Risk samples (`Red`, `Yellow`, `Green`). Can be marked as 'resolved' by administrators with specific notes.
*   **Twilio SMS Integration:** Configured in `utils.py` and `views.py`. Submitting a high-risk sample allows the system to text a fully customized warning to a saved phone number. 
*   **WhatsApp Links:** The frontend automatically generates clickable WhatsApp links to immediately message affected communities.

### E. Frontend Dashboard
*   **Summary Metrics:** Counts total samples, high-risk ratios, and active alerts.
*   **Data Visualizations:** Injects dynamically generated aggregates (like average pH and E.coli rates across all samples) into a Radar/Spider Chart.

---

## 3. Current "Level" of Completion
The project is currently at an **Advanced Prototype / MVP (Minimum Viable Product)** stage. 
It is fully operational for local testing and hackathon demonstrations.

### Features Working Flawlessly:
1.  **Form Submission to Database:** Users can submit sample metrics and they save perfectly.
2.  **ML Risk Generation:** The logistic regression engine correctly outputs tailored risk scores.
3.  **Local Server Stability:** The Django app boots cleanly with 0 PEP8/Flake8 style violations.
4.  **Dashboard Rendering:** Template context flows accurately to the frontend screens.

### Areas Currently Pending (Future Roadmap):
1.  **Cloud Database Deployment:** Currently bound to a local `db.sqlite3`. Moving to Neon/Supabase is required for cross-device usage.
2.  **API Externalization (REST):** The `django-rest-framework` is installed but no strict JSON endpoints (like `/api/samples`) have been fully documented for mobile app ingestion yet.
3.  **Advanced ML Models:** The current prediction model is trained on a synthetic dataset (`train_waterborne_model.py`). Upgrading to live census datasets would improve its accuracy in production.
