from rest_framework import generics
from .models import Review, ReviewComment, UserReview, UserReviewComment
from .serializers import ReviewSerializer, ReviewCommentSerializer, UserReviewSerializer, UserReviewCommentSerializer
from rest_framework.permissions import IsAuthenticated

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCommentCreateView(generics.CreateAPIView):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        review_id = self.kwargs['review_id']
        review = Review.objects.get(id=review_id)
        serializer.save(user=self.request.user, review=review)


class UserReviewCreateView(generics.CreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserReviewListView(generics.ListAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer


class UserReviewCommentCreateView(generics.CreateAPIView):
    queryset = UserReviewComment.objects.all()
    serializer_class = UserReviewCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        review_id = self.kwargs['review_id']
        review = UserReview.objects.get(id=review_id)
        serializer.save(user=self.request.user, user_review=review)
