from django.db import models
from django.contrib.auth.models import User

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.company_name


class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pay_rate = models.CharField(max_length=255)
    working_days = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=100)
    address = models.CharField(max_length=255, default='No address provided')
    employer_profile = models.ForeignKey('EmployerProfile', on_delete=models.CASCADE)
    document = models.FileField(upload_to='jobpost_documents/', null=True, blank=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, related_name='applications', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    documents = models.FileField(upload_to='documents/', null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.user.username} for {self.job_post.title}"
