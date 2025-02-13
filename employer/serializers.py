from rest_framework import serializers
from .models import EmployerProfile, JobPost, JobApplication

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'logo']

class JobPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = JobPost
        fields = ['id', 'title', 'description', 'pay_rate', 'working_days', 'working_hours', 'address', 'employer_profile']

class JobApplicationSerializer(serializers.ModelSerializer):
    job_post = JobPostSerializer(read_only=True)
    
    class Meta:
        model = JobApplication
        fields = ['job_post', 'user', 'profile_picture', 'age', 'address', 'documents', 'applied_at']
