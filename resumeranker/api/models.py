from django.db import models

# Create your models here.


class JobDescription(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Resume for {self.job.title}"