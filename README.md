# Smart Resume Screening System

A Flask-based web application that uses Natural Language Processing to match resumes with job descriptions AND find matching jobs across popular job portals.

## Features

### 1. Resume Screening (Original)
- Upload resume files (PDF or DOCX format)
- Enter job description
- Extract text from resumes automatically
- Calculate matching score using TF-IDF and Cosine Similarity
- Display matching percentage with visual feedback

### 2. Job Matching (NEW) 🆕
- Upload resume to find matching jobs
- AI-powered skill extraction (40+ skills)
- Smart job recommendations with match scores
- Direct links to apply on:
  - 🔵 Naukri.com
  - 💼 LinkedIn
  - 🟢 Indeed
  - 🟠 Apna
  - 🔴 Foundit (Monster India)
- Mobile responsive design

## Project Structure

```
smart_resume_screening/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── resumes/               # Folder to store uploaded resumes
├── templates/
│   ├── index.html         # Homepage with upload form
│   └── result.html        # Results page with score
└── static/
    └── style.css          # Styling for the web pages
```

## Installation

1. Navigate to the project directory:
```bash
cd smart_resume_screening
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and go to:
```
http://127.0.0.1:5000/
```

3. **Two modes available:**

   **Mode 1: Resume Screening**
   - Upload a resume (PDF or DOCX)
   - Enter the job description
   - Click "Analyze Resume" to get matching score

   **Mode 2: Find Jobs** (Click "Find Jobs" button)
   - Upload your resume
   - AI extracts your skills
   - Get matched jobs with direct portal links
   - Apply on Naukri, LinkedIn, Indeed, Apna, Foundit

## Access on Mobile

1. Find your PC's IP address:
```bash
ipconfig
```

2. On mobile browser (same WiFi):
```
http://YOUR_IP_ADDRESS:5000
```

## How It Works

1. **Text Extraction**: Extracts text from PDF files using PyPDF2 and DOCX files using docx2txt
2. **Vectorization**: Converts resume and job description text into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency)
3. **Similarity Calculation**: Computes cosine similarity between the two vectors
4. **Score Display**: Shows the matching percentage (0-100%)

## Score Interpretation

- **70-100%**: Excellent Match - Highly suitable candidate
- **50-69%**: Good Match - Meets many requirements
- **30-49%**: Fair Match - Meets some requirements
- **0-29%**: Low Match - May not be suitable

## Technologies Used

- **Flask**: Web framework
- **scikit-learn**: Machine learning library for TF-IDF and cosine similarity
- **PyPDF2**: PDF text extraction
- **docx2txt**: DOCX text extraction
- **NLTK**: Natural Language Processing toolkit

## Notes

- Maximum file size: 16MB
- Supported formats: PDF, DOCX
- The application runs in debug mode by default (disable for production)
