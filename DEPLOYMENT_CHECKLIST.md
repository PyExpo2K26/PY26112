# 🚀 Quick Render Deployment Checklist

## Pre-Deployment (5 minutes)

- [ ] All code committed to GitHub
- [ ] `render.yaml` is in root directory
- [ ] `build.sh` makes executable: `chmod +x build.sh`
- [ ] `docs/requirements.txt` contains all dependencies
- [ ] No hardcoded secrets in code

## Deployment Steps (10-15 minutes)

### 1. Create Render Services
- [ ] Go to https://dashboard.render.com
- [ ] Click "New +" → "Blueprint"
- [ ] Connect your GitHub repository
- [ ] Authorize GitHub access
- [ ] Select this repository
- [ ] Click "Connect" and confirm

### 2. Wait for Auto-Deployment
- [ ] Monitor "Logs" tab for build/deploy progress
- [ ] Should take 2-5 minutes
- [ ] Look for "Deploy successful" message

### 3. Configure Environment Variables
- [ ] In Web Service → Environment tab
- [ ] Set `TWILIO_ACCOUNT_SID` (from Twilio)
- [ ] Set `TWILIO_AUTH_TOKEN` (from Twilio)
- [ ] Set `TWILIO_PHONE_NUMBER` (from Twilio)
- [ ] `DATABASE_URL` auto-linked to PostgreSQL
- [ ] `DJANGO_SECRET_KEY` auto-generated
- [ ] `DJANGO_DEBUG` = False (already set)

### 4. Verify Services Created
- [ ] Web Service (water-surveillance-portal) - should show "Live"
- [ ] PostgreSQL Database (water-surveillance-db) - should show "Available"
- [ ] Both services should have green status indicators

### 5. Run Migrations
- [ ] Go to Web Service → Shell tab
- [ ] Run: `python code/source/manage.py migrate`
- [ ] Run: `python code/source/manage.py createsuperuser` (optional, for admin)

### 6. Test Live Application
- [ ] Visit your app URL at: `https://water-surveillance-portal.onrender.com`
- [ ] Check that pages load correctly
- [ ] Test main features
- [ ] Monitor logs for errors

## Post-Deployment

### Optional: Add Custom Domain
- [ ] Go to Web Service → Custom Domain
- [ ] Add your domain
- [ ] Configure DNS records (Render will provide instructions)

### Continuous Deployment
- [ ] Any future `git push` to `main` automatically deploys
- [ ] Monitor status in Render dashboard

### Regular Maintenance
- [ ] Check logs regularly
- [ ] Monitor database usage
- [ ] Update dependencies as needed
- [ ] Keep Django and packages up to date

## Important Files Updated

✅ `render.yaml` - Added PostgreSQL service and environment variables
✅ `code/source/water_portal/settings.py` - Configured for production database
✅ `RENDER_DEPLOYMENT.md` - Complete deployment guide
✅ `.env.example` - Environment variable template

## Troubleshooting Quick Links

- Build failed? → Check Logs tab for detailed error
- Connection denied? → Verify DATABASE_URL in Environment tab
- Static files missing? → WhiteNoise is configured, run collectstatic if needed
- Application crash? → Check Logs for Django error messages

## Need Help?

- Full guide: See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)
- Render documentation: https://docs.render.com
- Django documentation: https://docs.djangoproject.com

---

**Estimated Time**: 15-20 minutes from start to live deployment ⏱️
