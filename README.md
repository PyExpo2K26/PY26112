# 💧 Water Surveillance Portal (WSP)

**Government Water Surveillance & Early Warning System**

The Water Surveillance Portal (WSP) is an AI-powered system designed to help government agencies, like the Department of Water Sanitation, monitor water quality, predict contamination outbreaks, and protect public health. By combining real-time data collection from field officers with advanced machine learning models, WSP acts as an early warning system against waterborne diseases.

---

## 🌟 Key Features

### 1. Advanced Water Sample Collection
Field officers can submit comprehensive water quality data from any location. The system tracks 18 distinct parameters:
*   **Location:** District, Village, Coordinates
*   **Physical:** Water Source, Turbidity (NTU)
*   **Chemical:** pH Level, Nitrates, Nitrites, Ammonia, Fluoride, Chloride, Sulphate
*   **Oxygen:** Dissolved Oxygen (DO), Biological Oxygen Demand (BOD), Chemical Oxygen Demand (COD)
*   **Heavy Metals:** Lead, Arsenic, Mercury, Cadmium, Iron
*   **Biological:** Presence of E.coli

### 2. AI-Powered Risk Prediction (Risk Engine)
The core of the system is the **Risk Engine**. It dynamically calculates a "Contamination Index" based on the submitted parameters and utilizes a Machine Learning model (Logistic Regression/Random Forest) to predict the probability of a waterborne disease outbreak. 
*   **Instant Scoring:** Every sample receives a calculated risk score (0% to 100%).
*   **Critical Thresholds:** Any sample scoring above 50% triggers a **Moderate Risk (Yellow)** alert, and anything above 70% triggers a **High Risk (Red)** alert. The presence of any toxic heavy metals instantly triggers a critical alert.

### 3. Automated System Alerts & Resolution
High-risk areas are immediately prioritized on the **Alerts Dashboard**.
*   **Tracking:** Active alerts show the affected village, district, and severity level.
*   **Actionable Resolution:** Once environmental issues are addressed, administrators can safely mark alerts as "Resolved" (Water is safe) using secure tracking interfaces.

### 4. Interactive Data Dashboard
A live dashboard visualizes the health of the entire water network:
*   **Overall Metrics:** Total samples tested, active alerts, and overall network safety percentage.
*   **Monthly Trends:** Line charts showing total tests vs. high-risk detections over time.
*   **Risk Radar:** A radar chart showing the average levels of critical contaminants (pH, Turbidity, DO, BOD, etc.).
*   **Regional Statistics:** Bar charts mapping highest-risk areas by district and water source type.

### 5. Smart Insights & Action Plans
The AI generates specific, targeted insights for every problematic sample:
*   **Identified Cause:** (e.g., "High Arsenic levels indicating industrial runoff.")
*   **Effect on Health:** (e.g., "Risk of long-term cumulative poisoning.")
*   **Immediate Remedy:** Suggested remediation actions for field teams (e.g., "Install reverse osmosis filters immediately.")

### 6. Emergency Notifications
A built-in notification system allows administrators to seamlessly send SMS/WhatsApp alerts directly to local contacts associated with contaminated water sources.

---

## 🛠️ Technology Stack

WSP is built with a robust, modern, and open-source technology stack:

### Backend Architecture
*   **Framework:** Django (Python) - robust, secure MVC framework.
*   **Database:** SQLite (default for development), migratable to PostgreSQL for production.
*   **Authentication:** Built-in Django Auth subsystem for Role-Based Access Control (Field Officers vs. Admins).
*   **Logic:** Custom `risk_engine.py` orchestrating scoring rules and ML inferences.

### Machine Learning (AI)
*   **Libraries:** `scikit-learn`, `pandas`, `numpy`
*   **Models:** `RandomForestClassifier` and `LogisticRegression`.
*   **Pipelines:** Training scripts (`train.py`) designed to ingest physical, chemical, and synthetic environmental data to calibrate the inference models dynamically. 

### Frontend & UI
*   **Templates:** Django Templating Language (HTML5).
*   **Styling:** Pure Vanilla CSS (Flexbox, CSS Grid) with a clean, highly-accessible, government-standard aesthetic (blues, clear typography).
*   **Interactivity:** Vanilla JavaScript for form validation, dynamic coordinate generation based on district selection, and asynchronous AJAX calls.
*   **Data Visualization:** `Chart.js` integrated for rendering interactive radar, line, and bar charts securely passing JSON-serialized data from the Python backend.

---

## 🚀 Installation & Setup

To run the WSP project locally on a Windows machine:

1. **Clone the Repository** (or navigate to the project directory).
2. **Set up a Virtual Environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install django scikit-learn pandas numpy
   ```
4. **Train the ML Model** (Initial generation of synthetic data and `.pkl` models):
   ```bash
   python source/ml/train.py
   python Backend/train_waterborne_model.py
   ```
5. **Set up the Database**:
   ```bash
   cd source
   python manage.py makemigrations monitoring
   python manage.py migrate
   ```
6. **(Optional) Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
8. **Access the Portal**: Open a web browser and navigate to `http://127.0.0.1:8000/`.
