# Installation Guide - Waterborne Disease Health Monitoring System

## System Requirements

### Minimum Requirements
- Python 3.10+
- 2GB RAM
- 500MB disk space
- Windows, macOS, or Linux

### Recommended Requirements
- Python 3.13+
- 4GB RAM
- 1GB disk space
- SSD for faster performance

## Installation Steps

### 1. Clone/Copy the Project

```bash
cd source/backend/Health_Monitoring_System
```

### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

Create a `requirements.txt` in the backend directory:

```
Django==5.0.0
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.24.3
scipy==1.11.4
```

Then install:
```bash
pip install -r requirements.txt
```

### 4. Configure Database

Run migrations to create database:
```bash
python manage.py migrate
```

### 5. Populate Waterborne Diseases

Load disease data into database:
```bash
python manage.py populate_waterborne_diseases
```

Expected output:
```
Successfully created Cholera
Successfully created Typhoid
Successfully created Hepatitis A
Successfully created Dysentery
Successfully created Giardiasis
Successfully created E. coli Infection
All waterborne diseases have been populated successfully!
```

### 6. Create Superuser (Admin)

For Django admin access:
```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Access the application:
- **Web App**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## Configuration Files

### settings.py Key Settings

```python
# Security
SECRET_KEY = 'your-secret-key-here'  # Change in production
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ML Model Path
WATERBORNE_ARTIFACTS_PATH = r'path\to\waterborne_artifacts.pkl'
```

## Troubleshooting

### ImportError: No module named 'sklearn'
```bash
pip install scikit-learn
```

### Database Error
```bash
python manage.py migrate --run-syncdb
```

### Port Already in Use
Use a different port:
```bash
python manage.py runserver 8080
```

### Model Not Found
Ensure `waterborne_artifacts.pkl` is in the correct path specified in `settings.py`

## Development Setup

### Running Tests
```bash
python manage.py test
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

### Creating Backup of Database
```bash
cp db.sqlite3 db.sqlite3.backup
```

## Production Deployment

### Important Security Changes

1. **Update SECRET_KEY**
   ```python
   SECRET_KEY = os.environ.get('SECRET_KEY', 'your-new-secret-key')
   ```

2. **Set DEBUG to False**
   ```python
   DEBUG = False
   ```

3. **Configure ALLOWED_HOSTS**
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **Update Database** (Use PostgreSQL recommended)
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'health_monitoring',
           'USER': 'postgres',
           'PASSWORD': 'your-password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Using Gunicorn

```bash
pip install gunicorn
gunicorn Health_Monitoring_System.wsgi:application --bind 0.0.0.0:8000
```

### Using Nginx

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /static {
        alias /path/to/static;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

## Environment Variables

Create `.env` file:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@host:port/dbname
LOG_LEVEL=INFO
```

## First Time Setup Checklist

- [ ] Python 3.13+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed from requirements.txt
- [ ] Database migrations applied
- [ ] Waterborne diseases populated
- [ ] Superuser created
- [ ] Development server runs successfully
- [ ] Can access http://localhost:8000
- [ ] Can access admin at http://localhost:8000/admin
- [ ] Model artifacts properly loaded

## Database Backup

Automatic backup before major changes:
```bash
python manage.py dumpdata > backup_$(date +%Y%m%d_%H%M%S).json
```

Restore from backup:
```bash
python manage.py loaddata backup_20260206_120000.json
```

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [scikit-learn Guide](https://scikit-learn.org/stable/documentation.html)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Version**: 1.0  
**Last Updated**: February 6, 2026
