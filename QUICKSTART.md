# 🚀 Quick Start Guide - Enhanced Resume Screening System

## What's New?

Your project now has **TWO POWERFUL FEATURES**:

### 1️⃣ Resume Screening (Original)
Compare a resume with a specific job description

### 2️⃣ Job Finder (NEW!)
Upload resume → Get matching jobs → Apply on top portals

---

## How to Run

```bash
cd smart_resume_screening
python app.py
```

Open: `http://localhost:5000`

---

## Feature 1: Resume Screening

**Use Case:** You have a job description and want to check if a resume matches

**Steps:**
1. Click "Resume Screening" (homepage)
2. Upload resume (PDF/DOCX)
3. Paste job description
4. Get match score (0-100%)

**Example:**
- Upload: Software_Engineer_Resume.pdf
- Job Description: "Looking for Python developer with Django experience..."
- Result: 75% Match ✅

---

## Feature 2: Job Finder (NEW!)

**Use Case:** You have a resume and want to find matching jobs

**Steps:**
1. Click "Find Jobs" button
2. Upload resume (PDF/DOCX)
3. AI extracts skills automatically
4. See top 5 matching jobs
5. Click portal buttons to apply

**Example:**
- Upload: Your_Resume.pdf
- Detected Skills: Python, Django, SQL, AWS
- Matched Jobs: 
  - Python Developer (85% match)
  - Full Stack Developer (70% match)
  - Backend Engineer (65% match)
- Apply on: Naukri | LinkedIn | Indeed | Apna | Foundit

---

## Job Portal Integration

When you click a portal button, it opens that job portal with:
- ✅ Job title pre-filled
- ✅ Location pre-filled
- ✅ Ready to search/apply

**Supported Portals:**
1. **Naukri.com** - India's largest job portal
2. **LinkedIn** - Professional networking
3. **Indeed** - Global job search
4. **Apna** - Quick jobs for all
5. **Foundit** - Career opportunities

---

## Skills Detected (40+)

**Programming Languages:**
Python, Java, JavaScript, C++, C#, PHP, Ruby, Go, Rust, TypeScript

**Frameworks:**
React, Angular, Vue, Django, Flask, Spring, Node.js

**Databases:**
SQL, MySQL, PostgreSQL, MongoDB, Oracle, Redis, Elasticsearch

**Cloud & DevOps:**
AWS, Azure, Docker, Kubernetes, CI/CD, DevOps

**Data Science & ML:**
Machine Learning, Data Science, TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy

**Others:**
HTML, CSS, REST API, GraphQL, Microservices, Git, Agile, Scrum

---

## Sample Jobs in Database

1. Python Developer - Bangalore
2. Full Stack Developer - Mumbai
3. Data Scientist - Hyderabad
4. Java Backend Developer - Pune
5. DevOps Engineer - Delhi
6. Frontend Developer - Bangalore
7. Machine Learning Engineer - Bangalore
8. Database Administrator - Chennai

**Note:** You can add more jobs by editing `jobs_db` in `app.py`

---

## Project Structure

```
smart_resume_screening/
├── app.py                      # Main backend (UPDATED)
├── requirements.txt            # Dependencies
├── README.md                   # Full documentation
├── JOB_INTEGRATION.md         # Job feature guide
├── resumes/                    # Uploaded resumes
├── templates/
│   ├── index.html             # Resume screening page (UPDATED)
│   ├── result.html            # Score display
│   ├── find_jobs.html         # Job finder page (NEW)
│   └── job_results.html       # Job matches page (NEW)
└── static/
    ├── style.css              # Styling (UPDATED)
    └── script.js              # Interactivity
```

---

## Mobile Access

1. Run on PC: `python app.py`
2. Find PC IP: `ipconfig` → Look for IPv4 (e.g., 192.168.1.5)
3. On mobile (same WiFi): `http://192.168.1.5:5000`

---

## Testing Tips

**Test Resume Screening:**
- Use any resume + job description
- Check if score makes sense

**Test Job Finder:**
- Upload resume with clear skills (Python, Java, etc.)
- Should detect skills and show matching jobs
- Click portal buttons to verify links work

---

## Troubleshooting

**No skills detected?**
- Make sure resume has clear skill keywords
- Check if file text extraction worked

**No jobs matched?**
- Resume skills don't match job database
- Add more jobs to `jobs_db` in app.py

**Portal links not working?**
- Links open job portal search pages
- You may need to refine search on the portal

---

## Next Steps

🎯 **Enhance the system:**
1. Add more jobs to database
2. Add more skills to detection
3. Integrate real job APIs (advanced)
4. Add user authentication
5. Save job applications
6. Email notifications

---

## Support

For issues or questions:
1. Check README.md
2. Check JOB_INTEGRATION.md
3. Review app.py code comments

---

**🎉 Your Smart Resume Screening System is now a complete Job Matching Platform!**

Enjoy finding the perfect job matches! 🚀
