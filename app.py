from flask import Flask, render_template, request
import os
import nltk
from PyPDF2 import PdfReader

nltk.download('punkt')

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Skill keywords database
SKILLS_DB = [
    "python", "java", "c++", "html", "css", "javascript",
    "flask", "django", "mysql", "mongodb", "git",
    "machine learning", "data analysis", "nlp",
    "react", "node", "api"
]

def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_skills(text):
    skills_found = []
    for skill in SKILLS_DB:
        if skill in text:
            skills_found.append(skill)
    return list(set(skills_found))

@app.route('/', methods=['GET', 'POST'])
def index():
    resume_skills = []
    job_skills = []
    match_percentage = 0
    missing_skills = []

    if request.method == 'POST':
        resume_file = request.files['resume']
        job_description = request.form['job_desc'].lower()

        if resume_file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(file_path)

            resume_text = extract_text_from_pdf(file_path)
            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_description)

            if len(job_skills) > 0:
                matched = set(resume_skills) & set(job_skills)
                match_percentage = round((len(matched) / len(job_skills)) * 100, 2)
                missing_skills = list(set(job_skills) - set(resume_skills))

    return render_template(
        "index.html",
        resume_skills=resume_skills,
        job_skills=job_skills,
        match_percentage=match_percentage,
        missing_skills=missing_skills
    )

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    app.run(debug=True)
