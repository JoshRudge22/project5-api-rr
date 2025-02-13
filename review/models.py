from django.db import models
from django.contrib.auth.models import User
from employer.models import EmployerProfile
from profiles.models import Profile

class Review(models.Model):
    employer_profile = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.employer_profile.company_name} by {self.user.username}"


class UserReview(models.Model):
    employer_profile = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    worker_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.worker_profile.user.username} by {self.employer_profile.company_name}"

class ReviewComment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on review by {self.review.user.username}"

class UserReviewComment(models.Model):
    user_review = models.ForeignKey(UserReview, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on worker review by {self.user_review.user.username}"
