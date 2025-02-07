from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly

class ProfileCreateUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        try:
            return self.request.user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=self.request.user)
            return profile

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        email = profile.user.email
        return Response({"email": email}, status=status.HTTP_200_OK)