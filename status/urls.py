from django.urls import path
from . import views

urlpatterns = [
    path('job/application/status/', views.JobApplicationStatusCreateView.as_view(), name='job-application-status-create'),
    path('job/application/statuses/', views.JobApplicationStatusListView.as_view(), name='job-application-status-list'),
]
