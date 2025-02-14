from rest_framework import serializers
from employer.models import JobApplication
from .models import JobApplicationStatus

class JobApplicationStatusSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job_application.job_post.title', read_only=True)
    user_name = serializers.CharField(source='job_application.user.username', read_only=True)

    class Meta:
        model = JobApplicationStatus
        fields = ['id', 'job_application', 'status', 'update_at', 'job_title', 'user_name']
