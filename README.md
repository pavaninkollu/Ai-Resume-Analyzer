# 🤖 AI Resume Analyzer - Smart Resume & JD Matcher

AI Resume Analyzer is a smart Django-based web app that helps users compare their resumes with job descriptions using NLP and machine learning. It scores the match and gives actionable suggestions for improvement.

---

## ✨ Features

- Upload resume (PDF/TXT/DOCX)
- Upload job description (JD)
- NLP-powered similarity score (TF-IDF + cosine similarity)
- Visual skill match feedback
- AI suggestions to improve resume relevance
- Clean UI with dynamic results
- Admin panel for managing uploads and users (optional)

---

## 🧰 Technologies Used

- **Backend:** Django, Python
- **NLP & ML:** Scikit-learn, NLTK, SpaCy
- **Frontend:** HTML, CSS, Bootstrap
- **Visualization:** Matplotlib / Chart.js (optional)
- **Others:** Pandas, NumPy

---

## ⚙️ Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/ai-resume-analyzer.git
   cd ai-resume-analyzer
2. **Create a Virtual Environment & Install Requirements**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

3. **Apply Migrations**
   ```sh
   python manage.py migrate

4. **Create Superuser (Optional)**
   ```sh
   python manage.py createsuperuser

5. **Run the Server**
   ```sh
   python manage.py runserver

6. **Visit**
   ```sh
   http://127.0.0.1:8000/
