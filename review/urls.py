from django.urls import path
from . import views

urlpatterns = [
    path('company-review/create/', views.ReviewCreateView.as_view(), name='company-review-create'),
    path('company-reviews/', views.ReviewListView.as_view(), name='company-review-list'),
    path('company-review/<int:review_id>/comment/', views.ReviewCommentCreateView.as_view(), name='company-review-comment-create'),
    path('worker-review/create/', views.UserReviewCreateView.as_view(), name='worker-review-create'),
    path('worker-reviews/', views.UserReviewListView.as_view(), name='worker-review-list'),
    path('worker-review/<int:review_id>/comment/', views.UserReviewCommentCreateView.as_view(), name='worker-review-comment-create'),
]

