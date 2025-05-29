# AI Resume Analyzer

An intelligent web application built with **Django** that uses **NLP techniques** and **machine learning** to analyze resumes against job descriptions. The tool helps users evaluate how well their skills match job requirements and provides visual feedback to improve their resumes.

---

## Features

- Upload and parse resumes and job descriptions  
- Calculate similarity score using NLP and TF-IDF vectorization  
- Visualize skill matching with charts  
- Provide AI-powered suggestions to enhance resume relevance  
- Built with Python, Django, Scikit-learn, Matplotlib, and other libraries  

---

## Tech Stack

- Backend: Django, Python  
- NLP & ML: Scikit-learn, NLTK, SpaCy, Pandas, NumPy  
- Visualization: Matplotlib, Chart.js (optional)  
- Frontend: HTML, CSS, Bootstrap  

---

## Installation

1. Clone the repository  
```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
2. Create and activate a virtual environment  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Create a Virtual Environment & Activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set Up the Database:

bash
Copy
Edit
python manage.py migrate
Run the Development Server:

bash
Copy
Edit
python manage.py runserver
Open your browser and visit http://127.0.0.1:8000

Usage
Upload your resume and job description files.

The app calculates a similarity score showing how well your resume matches the job description.

View graphical charts that visualize skill matches.

Receive AI-powered suggestions to improve your resume relevance.

Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss.


