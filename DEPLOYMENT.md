# Deployment Guide - Host Your App Online

## Option 1: Render (Recommended - FREE)

### Steps:

1. **Create GitHub Account** (if you don't have)
   - Go to: https://github.com
   - Sign up for free

2. **Upload Your Project to GitHub**
   - Create new repository
   - Upload all project files
   - Or use GitHub Desktop

3. **Deploy on Render**
   - Go to: https://render.com
   - Sign up with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - Name: smart-resume-screening
     - Environment: Python 3
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
   - Click "Create Web Service"

4. **Your App is Live!**
   - URL: `https://your-app-name.onrender.com`
   - Share this link with anyone

**Pros:** Free, Easy, Auto-deploys on code changes
**Cons:** Sleeps after 15 min inactivity (free tier)

---

## Option 2: PythonAnywhere (FREE)

### Steps:

1. **Sign Up**
   - Go to: https://www.pythonanywhere.com
   - Create free account

2. **Upload Files**
   - Go to "Files" tab
   - Upload all project files
   - Or use "Upload a file" button

3. **Install Dependencies**
   - Go to "Consoles" → "Bash"
   - Run: `pip install --user flask scikit-learn PyPDF2 docx2txt`

4. **Configure Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Set path to your app.py
   - Click "Reload"

5. **Your App is Live!**
   - URL: `https://yourusername.pythonanywhere.com`

**Pros:** Free forever, Always on
**Cons:** Limited resources on free tier

---

## Option 3: Railway (FREE)

### Steps:

1. **Sign Up**
   - Go to: https://railway.app
   - Sign up with GitHub

2. **Deploy**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway auto-detects Flask app

3. **Your App is Live!**
   - Railway provides a URL
   - Click "Generate Domain"

**Pros:** Fast, Modern, Easy
**Cons:** Limited free hours per month

---

## Option 4: Heroku (Paid but Popular)

### Steps:

1. **Sign Up**
   - Go to: https://heroku.com
   - Create account

2. **Install Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

3. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

4. **Your App is Live!**
   - URL: `https://your-app-name.herokuapp.com`

---

## Quick Comparison

| Platform | Free Tier | Always On | Easy Setup |
|----------|-----------|-----------|------------|
| Render | ✅ Yes | ❌ Sleeps | ⭐⭐⭐⭐⭐ |
| PythonAnywhere | ✅ Yes | ✅ Yes | ⭐⭐⭐⭐ |
| Railway | ✅ Limited | ✅ Yes | ⭐⭐⭐⭐⭐ |
| Heroku | ❌ Paid | ✅ Yes | ⭐⭐⭐⭐ |

---

## Files Added for Deployment

✅ `Procfile` - Tells server how to run app
✅ `runtime.txt` - Specifies Python version
✅ `requirements.txt` - Updated with gunicorn
✅ `.gitignore` - Excludes unnecessary files

---

## After Deployment

Your app will be accessible at:
- `https://your-app-name.onrender.com` (Render)
- `https://yourusername.pythonanywhere.com` (PythonAnywhere)
- `https://your-app-name.up.railway.app` (Railway)

Share this URL with anyone to use your app!

---

## Troubleshooting

**App not starting?**
- Check logs in hosting platform
- Verify requirements.txt has all packages
- Ensure Procfile is correct

**Upload folder issues?**
- Some hosts have read-only filesystems
- May need to use temporary storage

**Slow performance?**
- Free tiers have limited resources
- Consider upgrading for production use
