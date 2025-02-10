from rest_framework import serializers
from .models import EmployerProfile, JobPost

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'logo']

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'pay_rate', 'working_days', 'working_hours', 'documents']