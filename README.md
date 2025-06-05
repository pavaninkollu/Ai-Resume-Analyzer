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




## 🧪 Usage
- Visit `http://127.0.0.1:8000/` in your browser.
- Upload your resume
- Upload a job description
- Click Analyze Button
- See:
      - Match score (e.g. 72%)
      - atched vs missing keywords
      - Suggestions to improve your resume

## Screenshots

![Login-ResumeReader](https://github.com/user-attachments/assets/d29652da-745f-41da-9a46-bb7818b2320c)
![Register-ResumeReader](https://github.com/user-attachments/assets/61c797a4-a6a6-45ed-bd3d-ae07c5b84e49)
![Upload-Resume-ResumeReader](https://github.com/user-attachments/assets/86a111df-c29e-4e77-a47b-758e971a9a81)
![ATS-Results-ResumeReader](https://github.com/user-attachments/assets/6996f4aa-1f47-4a04-bb1a-6e0e76128603)

## 📽️ Demo Video

<video width="700" controls>
  <source src="assets/E-commerce Site (1).mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss.



## Contact
For any queries, reach out to `pavankumarinkollu@gmail.com`.

