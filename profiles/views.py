from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter


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

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ['user__username', 'preferred_role', 'age', 'address', 'looking_for_work']

    def get_queryset(self):
        queryset = super().get_queryset()
        looking_for_work = self.request.query_params.get('looking_for_work', None)
        if looking_for_work:
            queryset = queryset.filter(looking_for_work=looking_for_work)
        preferred_role = self.request.query_params.get('preferred_role', None)
        if preferred_role:
            queryset = queryset.filter(preferred_role=preferred_role)

        return queryset

