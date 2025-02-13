from django.contrib import admin
from .models import Review, ReviewComment, UserReview, UserReviewComment

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'employer_profile', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('employer_profile__company_name', 'user__username', 'comment')

admin.site.register(Review, ReviewAdmin)

class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'employer_profile', 'worker_profile', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('worker_profile__user__username', 'employer_profile__company_name', 'comment')

admin.site.register(UserReview, UserReviewAdmin)

class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'user', 'created_at')
    search_fields = ('review__user__username', 'user__username', 'comment')

admin.site.register(ReviewComment, ReviewCommentAdmin)

class UserReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_review', 'user', 'created_at')
    search_fields = ('user_review__worker_profile__user__username', 'user__username', 'comment')

admin.site.register(UserReviewComment, UserReviewCommentAdmin)
