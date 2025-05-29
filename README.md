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

## Screenshots
![Upload-Resume-ResumeReader](https://github.com/user-attachments/assets/0ea2a70e-14ad-481e-860c-5cda58b4bfff)
![ATS-Results-ResumeReader](https://github.com/user-attachments/assets/3461bc29-9ecd-44ca-ad54-1a966332eb15)
![Login-ResumeReader](https://github.com/user-attachments/assets/04eddba4-24fd-4b0b-b40a-abb79bf4731d)
![Register-ResumeReader](https://github.com/user-attachments/assets/01a29d89-9d6b-4b43-beaa-8ec8accd22a1)

![Homepage](screenshots/homepage.png)

![Analysis Result](screenshots/analysis-result.png)

Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss.


