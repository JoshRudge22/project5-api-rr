from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import JobApplicationStatus
from .serializers import JobApplicationStatusSerializer

class JobApplicationStatusCreateView(generics.CreateAPIView):
    serializer_class = JobApplicationStatusSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        job_application = serializer.validated_data.get('job_application')
        status = serializer.validated_data.get('status')
        existing_status = JobApplicationStatus.objects.filter(job_application=job_application).first()

        if existing_status:
            existing_status.status = status
            existing_status.save()
            return Response({
                "id": existing_status.id,
                "status": existing_status.status,
                "update_at": existing_status.update_at
            }, status=status.HTTP_200_OK)
        serializer.save()
        return Response({
            "id": serializer.instance.id,
            "status": serializer.instance.status,
            "update_at": serializer.instance.update_at
        }, status=status.HTTP_201_CREATED)

class JobApplicationStatusListView(generics.ListAPIView):
    serializer_class = JobApplicationStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobApplicationStatus.objects.filter(job_application__user=self.request.user).order_by('-update_at')
