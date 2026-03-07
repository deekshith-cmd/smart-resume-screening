# Frontend-Backend Connection Guide

## Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        FRONTEND                              │
├─────────────────────────────────────────────────────────────┤
│  templates/index.html  →  Upload Form                       │
│  templates/result.html →  Display Score                     │
│  static/style.css      →  Styling                           │
│  static/script.js      →  Interactivity                     │
└─────────────────────────────────────────────────────────────┘
                            ↕
                    HTTP Requests
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                        BACKEND                               │
├─────────────────────────────────────────────────────────────┤
│  app.py                →  Flask Server                      │
│  Route: /              →  Serves index.html                 │
│  Route: /analyze       →  Processes resume                  │
│  extract_text()        →  Extracts PDF/DOCX text           │
│  calculate_similarity()→  Computes match score              │
└─────────────────────────────────────────────────────────────┘
```

## How They Connect

### 1. Homepage (/)
**Frontend:** `index.html`
- User sees upload form
- Form action="/analyze" method="POST"

**Backend:** `app.py`
```python
@app.route('/')
def index():
    return render_template('index.html')
```

### 2. Form Submission (/analyze)
**Frontend:** `index.html`
- User uploads resume file
- User enters job description
- Clicks "Analyze Resume" button
- Form sends POST request to /analyze

**Backend:** `app.py`
```python
@app.route('/analyze', methods=['POST'])
def analyze():
    # Receives file and job description
    # Extracts text from resume
    # Calculates similarity score
    # Returns result.html with score
```

### 3. Result Display
**Frontend:** `result.html`
- Receives score from backend
- Displays percentage
- Shows color-coded feedback
- Provides "Analyze Another" button

**Backend:** `app.py`
```python
return render_template('result.html', score=score, filename=filename)
```

## Data Flow

```
User Action → Frontend Form → POST /analyze → Backend Processing
                                                      ↓
                                              Extract Text
                                                      ↓
                                              TF-IDF Vectorization
                                                      ↓
                                              Cosine Similarity
                                                      ↓
User Sees Result ← Frontend Display ← result.html ← Score Calculation
```

## File Connections

### index.html connects to:
- `style.css` via: `{{ url_for('static', filename='style.css') }}`
- `script.js` via: `{{ url_for('static', filename='script.js') }}`
- Backend `/analyze` via: `<form action="/analyze" method="POST">`

### result.html connects to:
- `style.css` via: `{{ url_for('static', filename='style.css') }}`
- Backend `/` via: `<a href="/" class="btn">`

### app.py serves:
- Static files from `/static` folder
- Templates from `/templates` folder
- Uploaded files saved to `/resumes` folder

## API Endpoints

| Method | Endpoint  | Purpose              | Returns        |
|--------|-----------|----------------------|----------------|
| GET    | /         | Homepage             | index.html     |
| POST   | /analyze  | Process resume       | result.html    |

## Technologies Used

**Frontend:**
- HTML5 (Structure)
- CSS3 (Styling + Responsive Design)
- JavaScript (Interactivity)

**Backend:**
- Flask (Web Framework)
- PyPDF2 (PDF Processing)
- docx2txt (DOCX Processing)
- scikit-learn (ML/NLP)

## How to Test the Connection

1. Start backend: `python app.py`
2. Open browser: `http://localhost:5000`
3. Upload a resume
4. Enter job description
5. Click "Analyze Resume"
6. See the result page with score

The frontend and backend are fully integrated and working together!
