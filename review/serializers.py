from rest_framework import serializers
from .models import Review, ReviewComment, UserReview, UserReviewComment
from employer.models import EmployerProfile
from profiles.models import Profile

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = ['user', 'comment', 'created_at']

class UserReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReviewComment
        fields = ['user', 'comment', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    comments = ReviewCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'employer_profile', 'user', 'rating', 'comment', 'created_at', 'comments']

class UserReviewSerializer(serializers.ModelSerializer):
    employer_profile = serializers.PrimaryKeyRelatedField(queryset=EmployerProfile.objects.all())
    worker_profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    rating = serializers.IntegerField()
    comment = serializers.CharField()

    class Meta:
        model = UserReview
        fields = ['employer_profile', 'worker_profile', 'rating', 'comment', 'created_at']
