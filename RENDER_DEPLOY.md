# Deploy to Render - Simple Steps

## What You Need:
1. GitHub account
2. Render account (free)

## Step-by-Step:

### 1. Create GitHub Repository

1. Go to https://github.com
2. Click "New repository"
3. Name it: `smart-resume-screening`
4. Click "Create repository"

### 2. Upload Your Code to GitHub

**Option A: Using GitHub Website**
1. Click "uploading an existing file"
2. Drag all files from `smart_resume_screening` folder
3. Click "Commit changes"

**Option B: Using Git Commands**
```bash
cd "c:\Users\prajwal gowda\OneDrive\Desktop\My Project\smart_resume_screening"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/smart-resume-screening.git
git push -u origin main
```

### 3. Deploy on Render

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with GitHub
4. Click "New +" → "Web Service"
5. Click "Connect account" to link GitHub
6. Find your `smart-resume-screening` repo
7. Click "Connect"

### 4. Configure Settings

Fill in these fields:
- **Name:** `smart-resume-screening`
- **Region:** Choose closest to you
- **Branch:** `main`
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Instance Type:** `Free`

Click "Create Web Service"

### 5. Wait for Deployment

- Render will install packages (2-5 minutes)
- Watch the logs
- When you see "Build successful", it's ready!

### 6. Access Your App

Your app URL will be:
```
https://smart-resume-screening-XXXX.onrender.com
```

Copy this URL and share it!

## Test Your Deployed App

1. Open the URL in browser
2. Try "Resume Screening" feature
3. Try "Find Jobs" feature
4. Test on mobile too!

## Important Notes

⚠️ **Free Tier Limitations:**
- App sleeps after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds
- 750 hours/month free

✅ **To Keep App Always Active:**
- Upgrade to paid plan ($7/month)
- Or use a service like UptimeRobot to ping your app

## Updating Your App

When you make changes:
1. Update files on GitHub
2. Render auto-deploys new version
3. Wait 2-3 minutes
4. Refresh your app URL

## Done!

Your app is now live and accessible worldwide! 🎉

Share the URL with anyone to use your Smart Resume Screening System!
