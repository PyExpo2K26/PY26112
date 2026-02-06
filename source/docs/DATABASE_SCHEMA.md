# Database Schema Documentation

## Overview

The Waterborne Disease Health Monitoring System uses Django ORM with SQLite3 as the default database. The schema includes user authentication (Django built-in) and custom models for disease information and patient data.

## Database Diagram

```
┌─────────────────────────────┐
│        auth_user            │
├─────────────────────────────┤
│ id (PK)                     │
│ username (UNIQUE)           │
│ password (hashed)           │
│ email (UNIQUE)              │
│ first_name                  │
│ last_name                   │
│ is_staff                    │
│ is_active                   │
│ date_joined                 │
└──────────────┬──────────────┘
               │
               │ (Django relation)
               │
┌──────────────▼──────────────┐
│     web_diseaseinfo         │
├─────────────────────────────┤
│ id (PK)                     │
│ name (UNIQUE)               │
│ remedy (TEXT)               │
│ bio_profile (JSON TEXT)     │
└─────────────────────────────┘
```

## Table: auth_user (Django Built-in)

**Purpose**: Store user credentials and profile information

**Columns**:
```sql
CREATE TABLE auth_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME,
    is_superuser BOOLEAN NOT NULL DEFAULT 0,
    username VARCHAR(150) NOT NULL UNIQUE,
    first_name VARCHAR(150) NOT NULL DEFAULT '',
    last_name VARCHAR(150) NOT NULL DEFAULT '',
    email VARCHAR(254) NOT NULL UNIQUE,
    is_staff BOOLEAN NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    date_joined DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

**Description**:
- `id`: Unique user identifier (auto-increment)
- `password`: Hashed password using Django's default hasher (PBKDF2)
- `last_login`: Timestamp of last authentication
- `is_superuser`: Boolean flag for admin users
- `username`: Unique username for login
- `first_name`: User's first name (optional)
- `last_name`: User's last name (optional)
- `email`: Unique email address
- `is_staff`: Flag for staff access (admin panel)
- `is_active`: Soft delete flag (False = account disabled)
- `date_joined`: Account creation timestamp

**Example Data**:
```
id | username    | email              | is_active | date_joined
1  | john_doe    | john@example.com   | 1         | 2026-02-06
2  | jane_smith  | jane@example.com   | 1         | 2026-02-06
```

---

## Table: web_diseaseinfo (Custom Model)

**Purpose**: Store waterborne disease information and clinical data

**Model Definition**:
```python
class DiseaseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    remedy = models.TextField()
    bio_profile = models.TextField(help_text="JSON-like string")
    
    class Meta:
        app_label = 'web'
        
    def __str__(self):
        return self.name
```

**Database Schema**:
```sql
CREATE TABLE web_diseaseinfo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    remedy TEXT NOT NULL,
    bio_profile TEXT NOT NULL
);
```

**Column Details**:

### `id` (INTEGER PRIMARY KEY)
- Unique disease identifier
- Auto-incremented
- Range: 1-infinity

### `name` (VARCHAR(100) UNIQUE)
- Disease name
- Maximum 100 characters
- Must be unique across all diseases
- Examples:
  - "Cholera"
  - "Typhoid"
  - "Hepatitis A"
  - "Dysentery"
  - "Giardiasis"
  - "E. coli Infection"

### `remedy` (TEXT)
- Treatment recommendations and medical guidance
- No maximum length
- Rich text content
- Examples:

```
"Rehydration is the most important treatment. Rapidly replace fluids 
and electrolytes lost through diarrhea using Oral Rehydration Salts (ORS). 
In severe cases, intravenous fluids are required. Antibiotics 
(like tetracycline or doxycycline) can shorten the duration of the illness."
```

### `bio_profile` (TEXT - JSON Format)
- Biochemical values as JSON string
- Stored as TEXT but formatted as JSON
- Contains typical biochemical markers for the disease

**JSON Structure**:
```json
{
    "Sodium_mmol_L": 130.5,
    "Potassium_mmol_L": 3.1,
    "Chloride_mmol_L": 92.5,
    "WBC_109_per_L": 13.5,
    "Hemoglobin_g_dL": 13.8,
    "Platelets_109_per_L": 210.0,
    "Urea_mg_dL": 48.0,
    "Creatinine_mg_dL": 1.5,
    "Bilirubin_mg_dL": 0.9,
    "ALT_U_L": 40.0,
    "AST_U_L": 45.0
}
```

**Biochemical Parameters Definitions**:
```
Sodium_mmol_L        - Sodium concentration (electrolyte)
                       Normal: 135-145 mmol/L

Potassium_mmol_L     - Potassium concentration (electrolyte)
                       Normal: 3.5-5.0 mmol/L

Chloride_mmol_L      - Chloride concentration (electrolyte)
                       Normal: 98-106 mmol/L

WBC_109_per_L        - White blood cell count (infection indicator)
                       Normal: 4.5-11.0 × 10^9/L

Hemoglobin_g_dL      - Hemoglobin concentration (oxygen carrier)
                       Normal: 12.0-17.5 g/dL

Platelets_109_per_L  - Platelet count (clotting factor)
                       Normal: 150-400 × 10^9/L

Urea_mg_dL           - Blood urea nitrogen (kidney function)
                       Normal: 7-20 mg/dL

Creatinine_mg_dL     - Creatinine (kidney function indicator)
                       Normal: 0.6-1.2 mg/dL

Bilirubin_mg_dL      - Bilirubin (liver function - jaundice)
                       Normal: 0.1-1.2 mg/dL

ALT_U_L              - Alanine transaminase (liver enzyme)
                       Normal: 7-56 U/L

AST_U_L              - Aspartate transaminase (liver enzyme)
                       Normal: 10-40 U/L
```

---

## Example Data

### DiseaseInfo Records

#### Record 1: Cholera
```sql
INSERT INTO web_diseaseinfo (name, remedy, bio_profile) VALUES (
    'Cholera',
    'Rehydration is the most important treatment...',
    '{"Sodium_mmol_L": 130.5, "Potassium_mmol_L": 3.1, ...}'
);
```

#### Record 2: Hepatitis A
```sql
INSERT INTO web_diseaseinfo (name, remedy, bio_profile) VALUES (
    'Hepatitis A',
    'There is no specific antiviral treatment for Hepatitis A...',
    '{"Sodium_mmol_L": 139.0, "ALT_U_L": 847.0, "AST_U_L": 725.0, ...}'
);
```

---

## Queries

### Get User by Username
```sql
SELECT * FROM auth_user WHERE username = 'john_doe';
```

### Get All Active Diseases
```sql
SELECT id, name FROM web_diseaseinfo ORDER BY name;
```

### Get Disease Info with Parsing
```sql
SELECT 
    id, 
    name, 
    remedy,
    json_extract(bio_profile, '$.ALT_U_L') as ALT,
    json_extract(bio_profile, '$.AST_U_L') as AST
FROM web_diseaseinfo 
WHERE name = 'Hepatitis A';
```

### Count Users
```sql
SELECT COUNT(*) as total_users FROM auth_user WHERE is_active = 1;
```

### Get Disease with Highest Sodium Levels
```sql
SELECT 
    name,
    json_extract(bio_profile, '$.Sodium_mmol_L') as sodium
FROM web_diseaseinfo
ORDER BY json_extract(bio_profile, '$.Sodium_mmol_L') DESC
LIMIT 1;
```

---

## Indexes

For performance optimization, add indexes:

```sql
CREATE INDEX idx_auth_user_username ON auth_user(username);
CREATE INDEX idx_auth_user_email ON auth_user(email);
CREATE INDEX idx_diseaseinfo_name ON web_diseaseinfo(name);
```

---

## Data Validation

### auth_user Constraints
- `username`: NOT NULL, UNIQUE, VARCHAR(150)
- `email`: NOT NULL, UNIQUE, VARCHAR(254)
- `password`: NOT NULL (hashed)

### web_diseaseinfo Constraints
- `name`: NOT NULL, UNIQUE, VARCHAR(100)
- `remedy`: NOT NULL, TEXT
- `bio_profile`: NOT NULL, TEXT (valid JSON)

---

## Relationships

```
auth_user (1) ←→ (Many) Prediction Records
              │
              └─→ web_diseaseinfo (1) ←→ (Many) Prediction Records
```

While no explicit foreign key in current schema, relationships can be established:
- User can make multiple predictions
- Each prediction links to a disease

---

## Backup and Recovery

### Backup Database
```bash
# SQLite3 backup
sqlite3 db.sqlite3 ".dump" > backup.sql

# Or using Django
python manage.py dumpdata > backup.json
```

### Restore from Backup
```bash
# Restore from SQL dump
sqlite3 db.sqlite3 < backup.sql

# Restore from JSON
python manage.py loaddata backup.json
```

---

## Migration Management

### Create Migration (after model changes)
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### View Migration History
```bash
python manage.py showmigrations
```

### Rollback Migrations
```bash
python manage.py migrate web 0001
```

---

## Performance Considerations

1. **Indexing**: Add indexes on frequently queried columns
2. **Query Optimization**: Use select_related() for foreign keys
3. **Database Scaling**: Consider PostgreSQL for production
4. **Archiving**: Move old prediction records to archive table
5. **Partitioning**: Partition by date for time-series data

---

## Future Schema Extensions

### Potential Tables

```sql
-- For tracking predictions
CREATE TABLE prediction_log (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    disease_id INTEGER,
    symptoms TEXT,
    predicted_disease VARCHAR(100),
    confidence FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES auth_user(id),
    FOREIGN KEY(disease_id) REFERENCES web_diseaseinfo(id)
);

-- For water quality monitoring
CREATE TABLE water_quality (
    id INTEGER PRIMARY KEY,
    location VARCHAR(255),
    color VARCHAR(20),
    odor VARCHAR(20),
    ph_level FLOAT,
    turbidity FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- For outbreak tracking
CREATE TABLE outbreak_report (
    id INTEGER PRIMARY KEY,
    location VARCHAR(255),
    disease_id INTEGER,
    case_count INTEGER,
    report_date DATETIME,
    FOREIGN KEY(disease_id) REFERENCES web_diseaseinfo(id)
);
```

---

**Version**: 1.0  
**Last Updated**: February 6, 2026  
**Database**: SQLite3 (default), PostgreSQL (recommended for production)
