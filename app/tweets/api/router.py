from django.urls import path
from tweets.api.views import TweetListAPIView

urlpatterns = [
    path('tweets/<int:pk>/', TweetListAPIView.as_view()),
]