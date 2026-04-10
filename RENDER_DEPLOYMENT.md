# Render Deployment Guide - Water Surveillance Portal

## Prerequisites
- Render account (sign up at https://render.com)
- GitHub repository with your code
- Twilio account credentials (if using notifications)

---

## Step 1: Prepare Your Repository

Ensure your GitHub repository contains:
- ✅ `render.yaml` (configured blueprint)
- ✅ `build.sh` (build script)
- ✅ `code/source/` (Django project)
- ✅ `docs/requirements.txt` (Python dependencies)

Push all changes to GitHub:
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

---

## Step 2: Connect Repository to Render

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Blueprint"**
3. Select **"Connect a GitHub Repo"**
4. Authorize GitHub access if needed
5. Select your repository
6. Click **"Connect"**

---

## Step 3: Configure Environment Variables

After connecting, Render will create services from `render.yaml`. You need to set sensitive values:

### In the Render Dashboard:

1. **Navigate to your Web Service** (water-surveillance-portal)
2. Go to **Environment** tab
3. Add/Update these variables:

| Variable | Value | Source |
|----------|-------|--------|
| `TWILIO_ACCOUNT_SID` | Your Twilio SID | Twilio Console |
| `TWILIO_AUTH_TOKEN` | Your Twilio Auth Token | Twilio Console |
| `TWILIO_PHONE_NUMBER` | Your Twilio Phone Number | Twilio Console |
| `DATABASE_URL` | Auto-populated (linked to PostgreSQL) | Auto-linked from Database service |
| `DJANGO_SECRET_KEY` | Auto-generated | Already set |
| `DJANGO_DEBUG` | `False` | Already set |
| `DJANGO_ALLOWED_HOSTS` | Updated automatically | Auto-linked |

### To Link the Database:

1. Go to your **PostgreSQL service** in Render dashboard
2. Copy the **Internal Database URL**
3. In your **Web Service** Environment settings, add:
   - Key: `DATABASE_URL`
   - Value: Paste the PostgreSQL URL

---

## Step 4: Deploy

### Option A: Automatic Deployment (Recommended)
- Any push to `main` branch will trigger automatic deployment
- Monitor deployment in Render dashboard under **Logs**

### Option B: Manual Deploy
1. Go to your Web Service dashboard
2. Click **"Manual Deploy"** → **"Latest Commit"**
3. Wait for deployment to complete

---

## Step 5: Run Migrations (If Needed)

Once deployed:

1. Click your **Web Service** → **Shell** tab
2. Run:
```bash
python code/source/manage.py migrate
python code/source/manage.py createsuperuser  # Optional: create admin user
```

---

## Step 6: Verify Deployment

1. Check for any **build errors** in the Logs
2. Visit your app URL: `https://water-surveillance-portal.onrender.com`
3. Test the application
4. Monitor logs for any runtime errors

---

## Troubleshooting

### Build Failures
- Check logs: Web Service → **Logs** tab
- Verify `build.sh` runs correctly
- Ensure all dependencies in `requirements.txt` are compatible

### Database Connection Issues
- Verify `DATABASE_URL` is set in Environment variables
- Check PostgreSQL service is running (Services page)
- Ensure database migrations ran successfully (check Logs)

### Static Files Not Showing
- WhiteNoise is configured in settings.py (already done)
- Ensure `STATIC_ROOT` is correct
- Check logs for collectstatic errors

### Application Errors
- Check Render **Logs** for error messages
- Verify all environment variables are set
- Ensure Django settings are correct for production

---

## Project Structure (Verified for Deployment)

```
PY26112/
├── render.yaml                    ✅ Deployment configuration
├── build.sh                       ✅ Build commands
├── docs/
│   └── requirements.txt          ✅ Python dependencies
└── code/source/
    ├── manage.py                 ✅ Django CLI
    ├── water_portal/
    │   ├── settings.py          ✅ Updated for production
    │   ├── urls.py              ✅ Django URL configuration
    │   └── wsgi.py              ✅ WSGI entry point
    ├── monitoring/
    ├── surveillance/
    └── staticfiles/             ✅ Collected static files
```

---

## Key Changes Made for Deployment

### 1. **Database Configuration** (`settings.py`)
- Now uses PostgreSQL in production (via `DATABASE_URL`)
- Falls back to SQLite in development

### 2. **Environment Variables** (`render.yaml`)
- Added PostgreSQL service configuration
- Added Twilio secrets (configure in dashboard)
- All sensitive values use environment variables

### 3. **Build Process** (`build.sh`)
- Installs dependencies
- Collects static files
- Applies database migrations

---

## Useful Commands

### Access Remote Shell
```
Go to Render Dashboard → Web Service → Shell tab
```

### View Logs
```
Render Dashboard → Web Service → Logs tab
```

### Connect to PostgreSQL
```
Use the Internal Database URL provided in your PostgreSQL service details
```

### Manual Database Migration
```bash
python code/source/manage.py migrate
python code/source/manage.py createsuperuser
```

---

## Security Checklist

- ✅ `DEBUG = False` in production
- ✅ `DJANGO_SECRET_KEY` auto-generated
- ✅ Sensitive values use environment variables
- ✅ HTTPS enforced by Render
- ✅ ALLOWED_HOSTS configured
- ✅ CSRF trusted origins configured
- ✅ PostgreSQL replaces SQLite

---

## Support & Resources

- **Render Docs**: https://docs.render.com
- **Django Deployment**: https://docs.djangoproject.com/en/5.0/howto/deployment/
- **Gunicorn**: https://gunicorn.org/
- **WhiteNoise**: https://whitenoise.readthedocs.io/

---

**Last Updated**: April 2026
