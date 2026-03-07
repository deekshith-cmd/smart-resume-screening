# Job Portal Integration Guide

## 🎯 New Feature: Find Matching Jobs

Your Smart Resume Screening system now includes job matching functionality that connects with popular job portals!

## How It Works

### 1. Upload Resume
- User uploads their resume (PDF/DOCX)
- System extracts text automatically

### 2. AI Skill Extraction
- Automatically identifies skills from resume
- Recognizes 40+ technical skills including:
  - Programming: Python, Java, JavaScript, C++, etc.
  - Frameworks: React, Angular, Django, Flask, etc.
  - Databases: SQL, MongoDB, PostgreSQL, etc.
  - Cloud: AWS, Azure, Docker, Kubernetes
  - ML/AI: TensorFlow, PyTorch, Scikit-learn

### 3. Job Matching
- Compares resume skills with job database
- Calculates match percentage for each job
- Shows top 5 matching jobs

### 4. Portal Links
- Generates direct search links for:
  - **Naukri.com** - India's #1 job portal
  - **LinkedIn** - Professional networking
  - **Indeed** - Global job search
  - **Apna** - Blue & grey collar jobs
  - **Foundit** (Monster India) - Career opportunities

## Features

✅ **Automatic Skill Detection** - No manual input needed
✅ **Smart Job Matching** - AI-powered recommendations
✅ **Multi-Portal Integration** - Search across 5 platforms
✅ **Match Score** - See how well you fit each job
✅ **Direct Apply Links** - One-click access to job portals
✅ **Mobile Responsive** - Works on all devices

## Usage

### Access the Feature:
1. Go to homepage: `http://localhost:5000`
2. Click "Find Jobs" button
3. Upload your resume
4. View matched jobs with portal links

### Two Modes Available:

**Mode 1: Resume Screening** (Original)
- Compare resume with specific job description
- Get similarity score
- Route: `/`

**Mode 2: Find Jobs** (New)
- Upload resume to find matching jobs
- Get recommendations from job database
- Direct links to apply on portals
- Route: `/find-jobs`

## Technical Implementation

### Backend Functions:

```python
extract_skills(text)
# Extracts technical skills from resume text

get_job_recommendations(skills, resume_text)
# Matches skills with job database
# Returns top 5 jobs with match scores

generate_job_portal_links(job_title, location)
# Creates search URLs for all portals
```

### Job Database:
- Currently includes 8 sample jobs
- Can be expanded with real job APIs
- Stored in `jobs_db` list in app.py

### Portal Integration:
- Generates dynamic search URLs
- Opens in new tab
- Pre-filled with job title and location

## Customization

### Add More Skills:
Edit `skills_keywords` list in `extract_skills()` function

### Add More Jobs:
Edit `jobs_db` list in `get_job_recommendations()` function

### Add More Portals:
Edit `generate_job_portal_links()` function

## Future Enhancements

🔮 **Possible Upgrades:**
- Real-time job API integration
- Save favorite jobs
- Email job alerts
- Application tracking
- Salary insights
- Company reviews integration

## API Integration (Advanced)

To connect with real job portal APIs:

1. **Naukri API** - Requires partnership
2. **LinkedIn API** - OAuth authentication needed
3. **Indeed API** - Publisher account required

Note: Most job portals don't provide free public APIs. Current implementation uses search URLs which is the most practical approach.

## Benefits

👤 **For Job Seekers:**
- Save time searching multiple portals
- Get personalized job recommendations
- See match percentage before applying
- One-stop solution for job hunting

🏢 **For Recruiters:**
- Quick candidate-job matching
- Automated skill extraction
- Efficient screening process

## Testing

Test with sample resumes containing skills like:
- Python, Django, SQL
- JavaScript, React, Node.js
- Java, Spring, Microservices
- AWS, Docker, Kubernetes

The system will automatically detect skills and show matching jobs!

---

**Your resume screening system is now a complete job matching platform! 🚀**
