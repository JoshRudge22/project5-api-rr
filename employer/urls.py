from django.urls import path
from . import views

urlpatterns = [
    path('employer/profile/create/', views.EmployerProfileCreateView.as_view(), name='employer-profile-create'),
    path('employer/profile/detail/', views.EmployerProfileDetailView.as_view(), name='employer-profile-detail'),
    path('employer/job/post/', views.JobPostCreateView.as_view(), name='job-post-create'),
    path('employer/job/list/', views.JobPostListView.as_view(), name='job-post-list'),
]