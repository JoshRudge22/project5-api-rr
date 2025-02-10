from django.db import models
from django.contrib.auth.models import User

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.company_name

class JobPost(models.Model):
    employer_profile = models.ForeignKey(EmployerProfile, related_name="job_posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    pay_rate = models.CharField(max_length=255)
    working_days = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=255)
    documents = models.FileField(upload_to='job_documents/', blank=True, null=True)

    def __str__(self):
        return self.title
