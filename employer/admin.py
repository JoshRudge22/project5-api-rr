from django.contrib import admin
from .models import EmployerProfile, JobPost, JobApplication


class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pay_rate', 'working_days', 'working_hours', 'employer_profile', 'get_applicant_count')
    search_fields = ('title', 'description')
    list_filter = ('employer_profile',)
    

    def get_applicant_count(self, obj):
        return obj.applications.count()  
    get_applicant_count.short_description = 'Number of Applicants'

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_post', 'user', 'applied_at', 'age', 'address')
    search_fields = ('user__username', 'job_post__title')
    list_filter = ('job_post',)


admin.site.register(EmployerProfile)
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
