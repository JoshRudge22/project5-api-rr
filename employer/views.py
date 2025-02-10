from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import JobPost, EmployerProfile
from .serializers import JobPostSerializer, EmployerProfileSerializer
from rest_framework.permissions import IsAuthenticated


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
        serializer.save(employer_profile=employer_profile)

class JobPostListView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobPost.objects.all()