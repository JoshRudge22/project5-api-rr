from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileCreateUpdateView.as_view(), name='profile'),
]