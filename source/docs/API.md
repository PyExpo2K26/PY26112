# API Documentation - Waterborne Disease Prediction System

## Base URL
```
http://localhost:8000
```

## Authentication
All endpoints except `/signup` and `/login` require user authentication.

## Endpoints

### 1. Predict Waterborne Disease
**Endpoint**: `POST /predict/`

**Description**: Predicts waterborne disease based on symptoms and water quality indicators.

**Request Body** (Form Data):
```
Symptom_Text: string (required)
Water_Color: string (Clear/Turbid, default: Clear)
Water_Odor: string (None/Fishy/Musty, default: None)
Age: integer (optional, default: 25)
Gender: string (Male/Female, optional)
Water_Source: string (River/Tap/Well, optional)
Hygiene_Score: integer (1-5, optional, default: 3)
```

**Example Request**:
```html
<form method="POST" action="/predict/">
    <input type="text" name="Symptom_Text" placeholder="e.g., watery diarrhea, vomiting, dehydration" required>
    <select name="Water_Color">
        <option value="Clear">Clear</option>
        <option value="Turbid">Turbid</option>
    </select>
    <select name="Water_Odor">
        <option value="None">None</option>
        <option value="Fishy">Fishy</option>
        <option value="Musty">Musty</option>
    </select>
    <button type="submit">Predict</button>
</form>
```

**Response** (HTML rendered):
```
Disease Prediction: Cholera

Remedy:
Rehydration is the most important treatment. Rapidly replace fluids and 
electrolytes lost through diarrhea using Oral Rehydration Salts (ORS). 
In severe cases, intravenous fluids are required.

Biochemical Profile (Normal Values):
- Sodium (mmol/L): 130.5
- Potassium (mmol/L): 3.1
- Chloride (mmol/L): 92.5
- WBC (10^9/L): 13.5
- Hemoglobin (g/dL): 13.8
- Platelets (10^9/L): 210.0
- Urea (mg/dL): 48.0
- Creatinine (mg/dL): 1.5
```

**Status Codes**:
- `200 OK` - Successful prediction
- `400 Bad Request` - Missing required parameters
- `401 Unauthorized` - User not authenticated
- `500 Internal Server Error` - Model processing error

---

### 2. Home Page
**Endpoint**: `GET /`

**Description**: Main dashboard page (requires authentication).

**Response**: HTML page with navigation to prediction and user profile

**Status Codes**:
- `200 OK` - Success
- `302 Found` - Redirect to login (if not authenticated)

---

### 3. User Signup
**Endpoint**: `POST /signup/`

**Description**: Register new user account.

**Request Body** (Form Data):
```
username: string (required, unique)
email: string (required, unique, valid email)
password1: string (required, minimum 8 characters)
password2: string (required, must match password1)
```

**Example Request**:
```html
<form method="POST" action="/signup/">
    <input type="text" name="username" placeholder="Username" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="password1" placeholder="Password" required>
    <input type="password" name="password2" placeholder="Confirm Password" required>
    <button type="submit">Sign Up</button>
</form>
```

**Response**: 
- Success: Redirect to home page
- Error: Return signup form with error messages

**Validation Rules**:
- Username: 3-150 characters
- Email: Valid format
- Password: Minimum 8 characters, must not be all numeric

---

### 4. User Login
**Endpoint**: `GET/POST /login/`

**Description**: Authenticate user and create session.

**Request Body** (Form Data):
```
username: string (required)
password: string (required)
```

**Response**: 
- Success: Redirect to home page
- Invalid: Return login form with error message

---

## Disease Classes

The model can predict the following waterborne diseases:

1. **Cholera**
   - Typical Symptoms: Severe watery diarrhea, vomiting, muscle cramps, rapid dehydration
   - Water Indicators: Turbid water, fishy odor
   - Key Biochemical: Low sodium, elevated WBC, increased urea

2. **Typhoid**
   - Typical Symptoms: High fever, headache, weakness, rash
   - Water Indicators: May have normal appearance
   - Key Biochemical: Low WBC, elevated liver enzymes

3. **Hepatitis A**
   - Typical Symptoms: Jaundice, abdominal pain, nausea, dark urine
   - Water Indicators: Contaminated water source
   - Key Biochemical: Very high ALT/AST, elevated bilirubin

4. **Dysentery**
   - Typical Symptoms: Bloody diarrhea, cramping, fever
   - Water Indicators: Poor sanitation, turbid water
   - Key Biochemical: High WBC, normal electrolytes

5. **Giardiasis**
   - Typical Symptoms: Greasy diarrhea, stomach cramps, gas, bloating
   - Water Indicators: Well or river water sources
   - Key Biochemical: Normal electrolytes, normal WBC

6. **E. coli Infection**
   - Typical Symptoms: Watery/bloody diarrhea, cramping
   - Water Indicators: Contaminated sources
   - Key Biochemical: Low hemoglobin (in STEC), elevated creatinine

## Model Information

**Algorithm**: Random Forest Classifier (150 estimators)
**Features**: 106 total
  - 100 TF-IDF features (symptom text)
  - 6 clinical features (age, gender, water source, hygiene, water color, odor)

**Performance**:
- Training Accuracy: 100%
- Testing Accuracy: 72.73%
- Training Set: 54 samples
- Test Set: 15 samples

## Error Responses

### Invalid Symptom Text
```
Error: Please provide symptom information
```

### Model Not Loaded
```
Error: Model not loaded
```

### Database Connection Error
```
Error: Database connection failed. Please try again later.
```

## Input Examples

### Example 1: Cholera Prediction
```
Symptom_Text: "Severe watery diarrhea, vomiting, muscle cramps, rapid weight loss"
Water_Color: Turbid
Water_Odor: Fishy
```

### Example 2: Typhoid Prediction
```
Symptom_Text: "High fever for several days, headache, weakness, abdominal pain"
Water_Color: Clear
Water_Odor: None
```

### Example 3: Hepatitis A Prediction
```
Symptom_Text: "Jaundice, yellowing of eyes, dark urine, abdominal tenderness"
Water_Color: Clear
Water_Odor: None
```

## Rate Limiting

To prevent abuse, implement:
- 100 requests per hour per IP
- 10 requests per minute per user

## CORS Headers

For API integration:
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

## Response Headers

Standard headers in all responses:
```
Content-Type: text/html; charset=utf-8
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
```

## Versioning

Current API Version: **1.0**
- Base: `/api/v1/`
- Future versions: `/api/v2/`, etc.

## Changelog

### Version 1.0 (Feb 6, 2026)
- Initial release
- 6 waterborne disease predictions
- ML-based classification
- User authentication
- Web interface

---

## Integration Example (Python)

```python
import requests
from requests.auth import HTTPBasicAuth

# Login
session = requests.Session()
login_data = {
    'username': 'your_username',
    'password': 'your_password'
}
session.post('http://localhost:8000/login/', data=login_data)

# Make prediction
prediction_data = {
    'Symptom_Text': 'watery diarrhea, vomiting, dehydration',
    'Water_Color': 'Turbid',
    'Water_Odor': 'Fishy'
}
response = session.post('http://localhost:8000/predict/', data=prediction_data)
print(response.text)
```

---

**Last Updated**: February 6, 2026  
**API Version**: 1.0
