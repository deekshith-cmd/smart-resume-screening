from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import PyPDF2
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'resumes'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

ALLOWED_EXTENSIONS = {'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text(file_path):
    """Extract text from PDF or DOCX files"""
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    return ''

def calculate_similarity(resume_text, job_description):
    """Calculate cosine similarity between resume and job description"""
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)

def extract_skills(text):
    """Extract skills from resume text"""
    skills_keywords = [
        'python', 'java', 'javascript', 'react', 'angular', 'node', 'sql', 'mongodb',
        'aws', 'azure', 'docker', 'kubernetes', 'machine learning', 'data science',
        'html', 'css', 'flask', 'django', 'spring', 'git', 'agile', 'scrum',
        'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'typescript', 'vue',
        'mysql', 'postgresql', 'oracle', 'redis', 'elasticsearch',
        'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy',
        'rest api', 'graphql', 'microservices', 'devops', 'ci/cd'
    ]
    
    text_lower = text.lower()
    found_skills = [skill for skill in skills_keywords if skill in text_lower]
    return list(set(found_skills))[:10]  # Return top 10 unique skills

def get_job_recommendations(skills, resume_text):
    """Get job recommendations based on skills"""
    # Sample job database
    jobs_db = [
        {'title': 'Python Developer', 'company': 'Tech Corp', 'location': 'Bangalore', 'skills': ['python', 'django', 'sql'], 'description': 'Looking for Python developer with 2+ years experience'},
        {'title': 'Full Stack Developer', 'company': 'StartupXYZ', 'location': 'Mumbai', 'skills': ['javascript', 'react', 'node', 'mongodb'], 'description': 'Full stack developer needed for MERN stack projects'},
        {'title': 'Data Scientist', 'company': 'Analytics Inc', 'location': 'Hyderabad', 'skills': ['python', 'machine learning', 'tensorflow', 'pandas'], 'description': 'Data scientist role with ML expertise required'},
        {'title': 'Java Backend Developer', 'company': 'Enterprise Solutions', 'location': 'Pune', 'skills': ['java', 'spring', 'sql', 'microservices'], 'description': 'Java backend developer for enterprise applications'},
        {'title': 'DevOps Engineer', 'company': 'Cloud Systems', 'location': 'Delhi', 'skills': ['aws', 'docker', 'kubernetes', 'ci/cd'], 'description': 'DevOps engineer with cloud experience'},
        {'title': 'Frontend Developer', 'company': 'Design Studio', 'location': 'Bangalore', 'skills': ['react', 'javascript', 'html', 'css'], 'description': 'Frontend developer for modern web applications'},
        {'title': 'Machine Learning Engineer', 'company': 'AI Labs', 'location': 'Bangalore', 'skills': ['python', 'machine learning', 'pytorch', 'tensorflow'], 'description': 'ML engineer for AI product development'},
        {'title': 'Database Administrator', 'company': 'Data Corp', 'location': 'Chennai', 'skills': ['sql', 'mysql', 'postgresql', 'oracle'], 'description': 'DBA with expertise in database management'},
    ]
    
    # Calculate match score for each job
    matched_jobs = []
    for job in jobs_db:
        job_skills = set(job['skills'])
        resume_skills = set(skills)
        common_skills = job_skills.intersection(resume_skills)
        
        if common_skills:
            match_percentage = (len(common_skills) / len(job_skills)) * 100
            job_copy = job.copy()
            job_copy['match_score'] = round(match_percentage, 2)
            job_copy['matched_skills'] = list(common_skills)
            matched_jobs.append(job_copy)
    
    # Sort by match score
    matched_jobs.sort(key=lambda x: x['match_score'], reverse=True)
    return matched_jobs[:5]  # Return top 5 matches

def generate_job_portal_links(job_title, location):
    """Generate search links for popular job portals"""
    job_query = job_title.replace(' ', '%20')
    location_query = location.replace(' ', '%20')
    
    return {
        'naukri': f'https://www.naukri.com/{job_query}-jobs-in-{location_query}',
        'linkedin': f'https://www.linkedin.com/jobs/search/?keywords={job_query}&location={location_query}',
        'indeed': f'https://www.indeed.co.in/jobs?q={job_query}&l={location_query}',
        'apna': f'https://apna.co/jobs?title={job_query}&city={location_query}',
        'foundit': f'https://www.foundit.in/srp/results?query={job_query}&searchId=&locations={location_query}'
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find-jobs', methods=['GET', 'POST'])
def find_jobs():
    if request.method == 'GET':
        return render_template('find_jobs.html')
    
    if 'resume' not in request.files:
        return render_template('find_jobs.html', error='No file uploaded')
    
    file = request.files['resume']
    
    if file.filename == '':
        return render_template('find_jobs.html', error='No file selected')
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from resume
        resume_text = extract_text(filepath)
        
        if not resume_text.strip():
            return render_template('find_jobs.html', error='Could not extract text from resume')
        
        # Extract skills
        skills = extract_skills(resume_text)
        
        # Get job recommendations
        recommended_jobs = get_job_recommendations(skills, resume_text)
        
        # Add portal links to each job
        for job in recommended_jobs:
            job['portal_links'] = generate_job_portal_links(job['title'], job['location'])
        
        return render_template('job_results.html', 
                             jobs=recommended_jobs, 
                             skills=skills,
                             filename=filename)
    
    return render_template('find_jobs.html', error='Invalid file format. Only PDF and DOCX allowed')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return render_template('index.html', error='No file uploaded')
    
    file = request.files['resume']
    job_description = request.form.get('job_description', '')
    
    if file.filename == '':
        return render_template('index.html', error='No file selected')
    
    if not job_description.strip():
        return render_template('index.html', error='Job description is required')
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from resume
        resume_text = extract_text(filepath)
        
        if not resume_text.strip():
            return render_template('result.html', score=0, error='Could not extract text from resume')
        
        # Calculate similarity score
        score = calculate_similarity(resume_text, job_description)
        
        return render_template('result.html', score=score, filename=filename)
    
    return render_template('index.html', error='Invalid file format. Only PDF and DOCX allowed')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
