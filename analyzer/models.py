from django.db import models

class Resume(models.Model):
    
    name = models.CharField(max_length=255)
    resume_file = models.FileField(upload_to='resumes/')
    job_description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name