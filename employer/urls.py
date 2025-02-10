from django.urls import path
from . import views

urlpatterns = [
    path('employer/profile/create/', views.EmployerProfileCreateView.as_view(), name='employer-profile-create'),
    path('employer/profile/detail/', views.EmployerProfileDetailView.as_view(), name='employer-profile-detail'),
    path('employer/job/post/', views.JobPostCreateView.as_view(), name='job-post-create'),
    path('employer/job/list/', views.JobPostListView.as_view(), name='job-post-list'),
    path('job/application/<int:job_post_id>/', views.JobApplicationCreateView.as_view(), name='job-application-create'),
    path('job/applicants/<int:job_post_id>/', views.JobPostApplicantListView.as_view(), name='job-applicant-list'),
]