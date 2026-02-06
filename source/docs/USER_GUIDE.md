# User Guide - Waterborne Disease Health Monitoring System

## Getting Started

### System Access
1. Open web browser
2. Navigate to `http://localhost:8000`
3. You will be redirected to login page if not authenticated

## User Workflows

### 1. Creating an Account

**Steps**:
1. Click "Sign Up" link on login page
2. Enter your information:
   - **Username**: Choose a unique username (3-150 characters)
   - **Email**: Enter a valid email address
   - **Password**: Create a strong password (minimum 8 characters)
   - **Confirm Password**: Re-enter your password
3. Click "Sign Up" button
4. You will be logged in automatically
5. Dashboard will display

**Requirements**:
- Username must be unique
- Email must be valid and unique
- Passwords must match
- Password should be strong (recommended: mix uppercase, numbers, special chars)

---

### 2. Logging In

**Steps**:
1. Enter your username
2. Enter your password
3. Click "Login"
4. You will be redirected to the home page

**Forgot Password**:
- Contact system administrator
- Or use password reset function (if enabled)

---

## Disease Prediction Interface

### Predicting a Waterborne Disease

**Access**: Click "Predict Disease" button from home page

**Input Form**:

#### Required Fields
1. **Symptom Text**
   - Describe your symptoms in detail
   - Enter as free text
   - Examples:
     - "watery diarrhea, vomiting, severe dehydration"
     - "high fever for 3 days, headache, weakness"
     - "jaundice, yellow eyes, dark urine"
   
   **Tips**:
   - Be as specific as possible
   - Include duration and severity
   - Mention associated symptoms
   - Use medical terminology if familiar

#### Optional Fields
1. **Water Color** (Default: Clear)
   - Select from dropdown:
     - Clear - No visible contamination
     - Turbid - Cloudy, appears contaminated
   
   **Guidance**:
   - Observe the water source
   - Turbid water indicates possible contamination

2. **Water Odor** (Default: None)
   - Select from dropdown:
     - None - No unusual odor
     - Fishy - Indicates certain contaminants
     - Musty - Indicates organic matter/mold
   
   **Guidance**:
   - Smell the water cautiously
   - Any unusual odor suggests problems

3. **Age** (Default: 25)
   - Enter your age in years
   - Range: 0-120
   
4. **Gender** (Default: Male)
   - Select your gender:
     - Male
     - Female
   
5. **Water Source** (Default: Tap)
   - Select primary water source:
     - Tap - Piped municipal water
     - River - Surface water
     - Well - Ground water
   
   **Risk Assessment**:
   - Well & River: Higher contamination risk
   - Tap: Usually treated water, lower risk

6. **Hygiene Score** (Default: 3)
   - Rate your hygiene practices (1-5 scale):
     - 1 = Poor (no hand washing, poor sanitation)
     - 2 = Below average
     - 3 = Average
     - 4 = Good (regular hand washing, clean facilities)
     - 5 = Excellent (strict hygiene protocols)

### Submitting the Prediction

1. Fill in the "Symptom Text" field (required)
2. Optionally adjust other fields
3. Click "Predict" button
4. Results will display immediately

---

## Understanding Results

### Prediction Output

```
═════════════════════════════════════
PREDICTION RESULTS
═════════════════════════════════════

Disease Prediction: Cholera
───────────────────────────────────

TREATMENT RECOMMENDATIONS:
Rehydration is the most important treatment...
[Full remedy text]

───────────────────────────────────
BIOCHEMICAL PROFILE (Normal Values):
───────────────────────────────────
• Sodium (mmol/L): 130.5
• Potassium (mmol/L): 3.1
• Chloride (mmol/L): 92.5
• WBC (10^9/L): 13.5 (elevated - infection response)
• Hemoglobin (g/dL): 13.8
• Platelets (10^9/L): 210.0
• Urea (mg/dL): 48.0 (elevated - dehydration/kidney stress)
• Creatinine (mg/dL): 1.5
• Bilirubin (mg/dL): 0.9
• ALT (U/L): 40.0
• AST (U/L): 45.0

═════════════════════════════════════
```

### Interpreting Results

#### Disease Names
1. **Cholera** - Severe bacterial infection causing watery diarrhea
2. **Typhoid** - Sustained fever infection from contaminated water/food
3. **Hepatitis A** - Viral infection affecting the liver
4. **Dysentery** - Bacterial/parasitic infection with bloody diarrhea
5. **Giardiasis** - Parasitic infection from contaminated water
6. **E. coli Infection** - Bacterial infection with various presentations

#### Biochemical Value Interpretation

**Normal vs. Abnormal**:
```
Sodium 130.5 mmol/L
└─ ABNORMAL: Below normal range (135-145)
   Indicates electrolyte loss in cholera

WBC 13.5 × 10^9/L
└─ SLIGHTLY ELEVATED: Above normal (4.5-11.0)
   Indicates immune response to infection

Hemoglobin 13.8 g/dL
└─ NORMAL to SLIGHTLY HIGH: (12.0-17.5)
   May be elevated due to dehydration

Urea 48.0 mg/dL
└─ ELEVATED: Above normal (7-20)
   Indicates kidney stress or severe dehydration
```

---

## Disease-Specific Information

### Cholera
- **Cause**: Vibrio cholerae bacterium
- **Transmission**: Contaminated water/food
- **Incubation**: Few hours to 5 days
- **Danger**: Rapid dehydration and electrolyte loss
- **Prevention**:
  - Boil water before consumption
  - Practice good sanitation
  - Vaccination available
  - Proper food hygiene

### Typhoid
- **Cause**: Salmonella typhi bacterium
- **Transmission**: Contaminated water/food
- **Incubation**: 1-3 weeks
- **Symptoms Progress**: Gradually increasing fever
- **Prevention**:
  - Vaccination (recommended before travel)
  - Safe water practices
  - Food safety

### Hepatitis A
- **Cause**: Hepatitis A virus
- **Transmission**: Contaminated food/water
- **Incubation**: 15-50 days
- **Duration**: 2-12 weeks
- **Prevention**: Vaccination, hand hygiene
- **Note**: Usually self-limiting, rarely fatal

### Dysentery
- **Types**: Bacterial (Shigellosis) or Amoebic
- **Transmission**: Contaminated water/food
- **Danger**: Severe dehydration and nutritional loss
- **Prevention**: Safe water, sanitation, food hygiene

### Giardiasis
- **Cause**: Giardia parasite
- **Transmission**: Contaminated water (wells, streams)
- **Duration**: Can last weeks without treatment
- **Prevention**: Filter drinking water, boiling, hand hygiene
- **Treatment**: Antiparasitic medications

### E. coli Infection
- **Cause**: Enteroinvasive E. coli bacterium
- **Types**: STEC (causes hemorrhagic colitis) or other strains
- **Danger**: Risk of Hemolytic Uremic Syndrome (HUS)
- **Prevention**: Food safety, hygiene, clean water

---

## When to Seek Medical Attention

### SEEK IMMEDIATE CARE IF YOU EXPERIENCE:
- Blood in stool (especially with severe diarrhea)
- Persistent vomiting preventing fluid intake
- Severe abdominal pain
- Signs of shock (dizziness, confusion, weak pulse)
- Yellow eyes/skin (jaundice) with other symptoms
- Signs of severe dehydration:
  - Dry mouth
  - Dark urine
  - Dizziness
  - Extreme weakness

### CONTACT DOCTOR IF:
- Symptoms persist beyond 3 days
- Fever above 39°C (102°F)
- Unable to keep fluids down
- Symptoms worsen despite treatment
- Symptoms in children or elderly

---

## Emergency Contacts

**Local Health Department**: Contact your local health authority
**Emergency Services**: Call your country's emergency number:
- USA: 911
- Europe: 112
- India: 112
- Emergency hotline in your region

---

## Self-Care Recommendations

### Rehydration
```
Oral Rehydration Solution (ORS):
- 1 liter clean water
- 6 teaspoons sugar
- 1/2 teaspoon salt
- Drink small amounts frequently

OR use commercial ORS packets
```

### Diet During Illness
- **Start**: Sip water, apple juice, broth
- **Progress**: Plain rice, bananas, crackers
- **Avoid**: Dairy, spicy, fatty, high-fiber foods
- **Duration**: Gradually return to normal diet

### Hydration Guidelines
- **Cholera/Severe Diarrhea**: 1-2 liters ORS daily
- **Mild Diarrhea**: 500ml-1 liter additional fluids
- **Continue**: Until symptoms resolve

### Hygiene During Illness
- Wash hands after using bathroom
- Clean bathroom thoroughly
- Don't share utensils/towels
- Isolate from others if possible
- Drink safely treated water only

---

## Data Privacy

### Your Information
- Username, email, predictions stored securely
- Password never stored in plain text
- No data shared with third parties
- Uses Django's security framework

### Prediction Data
- Your prediction history is private
- Only visible to you and administrators
- Not used for non-medical purposes
- Compliance with health data regulations

---

## System Limitations

### Important Notes
1. **Not a Medical Diagnosis**: This system provides predictions based on ML models, not professional medical diagnosis
2. **Accuracy**: System accuracy is ~73% on test data, higher with detailed symptoms
3. **Incomplete Information**: Cannot validate all medical tests yourself
4. **Professional Review**: Predictions should be reviewed by healthcare professionals
5. **Emergency Situations**: Always call emergency services for severe symptoms

### Data Limitations
- Model trained on synthetic data
- May not capture all symptom presentations
- Rare disease variants not included
- Regional disease variations possible

---

## Frequently Asked Questions (FAQ)

### Q: How accurate is this system?
**A**: System accuracy is approximately 72.73% on independent test data. Provide detailed symptoms for better predictions. Always consult a healthcare professional for final diagnosis.

### Q: Can I use this instead of visiting a doctor?
**A**: No. This is a prediction tool to help identify potential waterborne diseases. Professional medical evaluation is essential for proper diagnosis and treatment.

### Q: How should I write the symptom text?
**A**: Be as specific and detailed as possible:
- Mention symptom severity (mild/moderate/severe)
- Include duration (how long symptoms have lasted)
- List all symptoms, not just primary ones
- Include associated signs (fever, weakness, etc.)

### Q: What if my symptoms don't match the results?
**A**: The system makes predictions based on pattern recognition. Symptoms can overlap between diseases. Consult a healthcare professional for confirmation.

### Q: Is my data secure?
**A**: Yes. Your account is protected with password hashing. Predictions are stored securely. No data is shared without consent.

### Q: Can I change my prediction?
**A**: You can make new predictions anytime. Previous predictions remain in your history for comparison.

### Q: What if I forgot my password?
**A**: Contact the system administrator for password reset assistance.

### Q: How often should I check my water quality?
**A**: Check water color and odor regularly (daily if possible). If changed or unusual, seek analysis or alternative water source.

### Q: Are the biochemical values from my blood?
**A**: No. The shown values are typical/average values for each disease based on research data, not your actual blood test results. Blood tests require laboratory analysis.

---

## Tips for Best Results

1. **Detail is Key**: Provide comprehensive symptom descriptions
2. **Timeline**: Include when symptoms started
3. **Severity**: Indicate how severe each symptom is
4. **Water Source**: Accurately describe your water source
5. **Hygiene**: Accurately assess your hygiene practices
6. **Physical Observations**: Note water color and odor if possible

---

## Technical Support

If you encounter issues:
1. Check Internet connection
2. Clear browser cache
3. Try different browser
4. Contact system administrator

---

## Version Information

**System Version**: 1.0  
**Last Updated**: February 6, 2026  
**Compatible Browsers**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

---

**Disclaimer**: This system is for informational purposes only. It is not a substitute for professional medical diagnosis and treatment. Always consult qualified healthcare professionals for medical advice.

**---**

*For technical documentation, see INSTALLATION.md, API.md, and ML_MODEL.md*
