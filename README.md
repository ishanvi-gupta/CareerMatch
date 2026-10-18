# CareerMatch – AI Resume Analyzer

CareerMatch is a Python-based web application that analyzes resumes and compares candidate skills with the requirements mentioned in a job description. It helps users identify matching and missing skills to better understand their suitability for a particular role.

## Features

- **Resume Upload:** Upload resumes in PDF format.
- **Skill Extraction:** Extract relevant skills from resumes and job descriptions.
- **Job Matching:** Calculate a match percentage based on the skills identified.
- **Missing Skills Detection:** Highlight skills required by the job that are absent from the resume.
- **Interactive Interface:** Analyze resumes through a simple web interface.

## Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Flask
- **NLP Library:** NLTK
- **PDF Processing:** PyPDF2
- **Frontend:** HTML, CSS
- **Concepts:** Natural Language Processing, Text Processing, Keyword Extraction, File Handling

## Installation and Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, create one containing:

```text
Flask
PyPDF2
nltk
```

### 2. Run the Application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

## How to Use

1. Open CareerMatch in your browser.
2. Upload your resume in PDF format.
3. Paste the job description into the provided text box.
4. Click **Analyze**.
5. Review your matching skills, match percentage, and missing skills.

## How It Works

CareerMatch extracts text from the uploaded PDF and processes it to identify predefined skill keywords. It performs the same skill extraction on the supplied job description, compares the two skill sets, and calculates the percentage of required skills found in the resume.

**Note:** The current version uses keyword-based matching and does not understand the full semantic meaning of a resume. The match percentage is an indicator of skill overlap, not a guarantee of job suitability.

## Future Enhancements

- Expand the skill database.
- Add support for DOCX resumes.
- Improve matching using semantic similarity and advanced NLP techniques.
- Add resume improvement suggestions.
- Introduce a visual analytics dashboard.
