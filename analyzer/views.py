from django.shortcuts import render, redirect
from .forms import ResumeForm
from .utils import (
    extract_resume_text, clean_and_tokenize, calculate_similarity_score,
    get_skill_match_data, generate_skill_match_chart, generate_wordcloud
)
import os
from django.http import HttpResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume_instance = form.save()
            file_path = resume_instance.resume_file.path

            # Extract raw text
            resume_text_raw = extract_resume_text(file_path)
            jd_text_raw = resume_instance.job_description

            resume_tokens = clean_and_tokenize(resume_text_raw)
            jd_tokens = clean_and_tokenize(jd_text_raw)

            score = calculate_similarity_score(resume_text_raw, jd_text_raw)
            matched_skills, missing_skills = get_skill_match_data(resume_text_raw, jd_text_raw)

            # Generate chart and wordclouds
            chart_path = os.path.join('media', 'skill_match_chart.png')
            resume_wc_path = os.path.join('media', 'resume_wc.png')
            jd_wc_path = os.path.join('media', 'jd_wc.png')
            generate_skill_match_chart(matched_skills, missing_skills, chart_path)
            generate_wordcloud(resume_text_raw, resume_wc_path)
            generate_wordcloud(jd_text_raw, jd_wc_path)

            matched_keywords_count = len(matched_skills)
            unmatched_keywords_count = len(missing_skills)
            resume_word_count = len(resume_text_raw.split())

            # Section-wise similarity
            sections = {
                'Skills': ('skills:', 'skills:'),
                'Experience': ('experience:', 'experience:'),
                'Education': ('education:', 'education:'),
                'Projects': ('projects:', 'projects:'),
                'Certifications': ('certifications:', 'certifications:')
            }

            def extract_section(text, start_marker):
                text = text.lower()
                start = text.find(start_marker)
                if start == -1:
                    return ''
                ends = [text.find(m[0], start + len(start_marker)) for m in sections.values()]
                ends = [e for e in ends if e != -1 and e > start]
                end = min(ends) if ends else len(text)
                return text[start:end].strip()

            section_scores = {}
            for name, (res_marker, jd_marker) in sections.items():
                resume_section = extract_section(resume_text_raw, res_marker)
                jd_section = extract_section(jd_text_raw, jd_marker)
                if resume_section and jd_section:
                    section_score = calculate_similarity_score(resume_section, jd_section)
                    section_scores[name] = round(section_score * 100, 2)
                else:
                    section_scores[name] = 0.0

            # Suggestions & tips generation
            suggestions = []
            if unmatched_keywords_count > 0:
                suggestions.append("Include more relevant keywords from the job description.")
            if section_scores.get('Skills', 0) < 60:
                suggestions.append("Update your skills section with more aligned technical terms.")
            if section_scores.get('Experience', 0) < 60:
                suggestions.append("Try to tailor your experience to better reflect the job role.")
            if resume_word_count < 150:
                suggestions.append("Resume is too short. Add more content if possible.")
            if resume_word_count > 700:
                suggestions.append("Resume is too long. Keep it concise and relevant.")

            if not suggestions:
                suggestions.append("Great job! Your resume is well-optimized.")

            return render(request, 'analyzer/result.html', {
                'resume_tokens': resume_tokens,
                'jd_tokens': jd_tokens,
                'score': score,
                'matched_skills': matched_skills,
                'missing_skills': missing_skills,
                'chart_url': '/' + chart_path,
                'resume_wc_url': '/' + resume_wc_path,
                'jd_wc_url': '/' + jd_wc_path,
                'matched_keywords_count': matched_keywords_count,
                'unmatched_keywords_count': unmatched_keywords_count,
                'resume_word_count': resume_word_count,
                'section_scores': section_scores,
                'resume_text': resume_text_raw,
                'suggestions': suggestions
            })
        else:
            print("Form Errors:", form.errors)
    else:
        form = ResumeForm()
    return render(request, 'analyzer/upload.html', {'form': form})

def download_report(request, score):
    report_text = f"Resume Matching Report\n\nScore: {score}%\n\nThank you for using our analyzer!"
    response = HttpResponse(report_text, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="resume_score_report.txt"'
    return response


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registreation Successful ! ')
            return redirect('login')
    
    else:
        form = UserCreationForm()
    return render(request, 'analyzer/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form  = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('upload_resume')
    else:
        form = AuthenticationForm()
    return render(request, 'analyzer/login.html', {'form': form})
        
def user_logout(request):
    logout(request)
    return redirect('login')
