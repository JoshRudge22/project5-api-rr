# status/models.py

from django.db import models
# Remove any imports of JobApplicationStatus here
from employer.models import JobApplication

class JobApplicationStatus(models.Model):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    job_application = models.ForeignKey(JobApplication, related_name="statuses", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.status} for {self.job_application.user.username} on {self.job_application.job_post.title}"
