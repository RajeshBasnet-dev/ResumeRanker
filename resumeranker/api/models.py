from django.db import models

# Create your models here.


class JobDescription(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    job = models.ForeignKey(JobDescription, related_name='resumes', on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    score = models.FloatField(default=0)

    def __str__(self):
        return f"Resume for {self.job.title}"