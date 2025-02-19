from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from .models import JobPost, EmployerProfile, JobApplication
from .serializers import JobPostSerializer, EmployerProfileSerializer, JobApplicationSerializer
from rest_framework.exceptions import PermissionDenied

class EmployerProfileCreateView(generics.CreateAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployerProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployerProfileSerializer
    queryset = EmployerProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return EmployerProfile.objects.get(user=self.request.user)


class JobPostCreateView(generics.CreateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            employer_profile = EmployerProfile.objects.get(user=self.request.user)
        except EmployerProfile.DoesNotExist:
            return Response(
                {"detail": "Employer profile not found. Please create a profile first."},
                status=status.HTTP_400_BAD_REQUEST
            )
        job_post = serializer.save(employer_profile=employer_profile)
        return Response(JobPostSerializer(job_post).data, status=status.HTTP_201_CREATED)


class JobPostListView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter,)
    search_fields = ['title', 'description', 'pay_rate', 'working_days', 'working_hours', 'address']  

    def get_queryset(self):
        queryset = JobPost.objects.all()
        return queryset


class JobApplicationCreateView(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        job_post_id = self.kwargs['job_post_id']
        user = self.request.user
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            job_post = JobPost.objects.get(id=job_post_id)
        except JobPost.DoesNotExist:
            return Response({"detail": "Job post not found."}, status=status.HTTP_400_BAD_REQUEST)
        job_application = serializer.save(
            job_post=job_post,
            user=user,
            profile_picture=profile.profile_picture,
            age=profile.age,
            address=profile.address,
            documents=profile.documents,
        )
        return Response(JobApplicationSerializer(job_application).data, status=status.HTTP_201_CREATED)


class JobPostApplicantListView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        job_post_id = self.kwargs['job_post_id']

        try:
            job_post = JobPost.objects.get(id=job_post_id)
        except JobPost.DoesNotExist:
            raise Response({"detail": "Job post not found."}, status=status.HTTP_404_NOT_FOUND)
        if job_post.employer_profile.user != self.request.user:
            raise PermissionDenied("You do not have permission to view applicants for this job post.")
        return JobApplication.objects.filter(job_post=job_post)
