import os
import docx2txt
from pdfminer.high_level import extract_text
import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from wordcloud import WordCloud

import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for Django
import matplotlib.pyplot as plt


COMMON_SKILLS = [
    'python', 'java', 'c++', 'django', 'flask', 'html', 'css', 'javascript',
    'react', 'node', 'sql', 'mysql', 'postgresql', 'mongodb', 'aws', 'docker',
    'kubernetes', 'git', 'linux', 'excel', 'pandas', 'numpy', 'matplotlib',
    'seaborn', 'tensorflow', 'nlp', 'data analysis', 'machine learning',
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in COMMON_SKILLS if skill in text]

def get_skill_match_data(resume_text, jd_text):
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    # Normalize text by removing punctuation
    translator = str.maketrans('', '', string.punctuation)
    resume_text = resume_text.translate(translator)
    jd_text = jd_text.translate(translator)

    matched_skills = []
    missing_skills = []

    for skill in COMMON_SKILLS:
        if skill in jd_text:
            if skill in resume_text:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

    return matched_skills, missing_skills

def generate_skill_match_chart(matched, missing, output_path):
    labels = ['Matched Skills', 'Missing Skills']
    counts = [len(matched), len(missing)]

    colors = ['green', 'red']

    plt.figure(figsize=(6, 4))
    plt.bar(labels, counts, color=colors)
    plt.title('Skill Match Overview')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def extract_resume_text(file_path):
    
    ext = os.path.splitext(file_path)[1]
    if ext =='.pdf':
        return extract_text(file_path)
    elif ext == '.docx':
        return docx2txt.process(file_path)
    else:
        return ""
    
def clean_and_tokenize(text):
    text = text.lower()
    tokens = word_tokenize(text)
    words = [word for word in tokens if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in words if not w in stop_words]
    return filtered

def calculate_similarity_score(resume_text, jd_text):
    resume_text = ' '.join(resume_text.split())
    jd_text = ' '.join(jd_text.split())

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = round(float(cosine_sim[0][0]) * 100)
    return score


def generate_wordcloud(text, output_path):
    if not text.strip():
        return  # Skip empty input
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    wc.to_file(output_path)
