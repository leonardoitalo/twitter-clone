from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, TweetViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'tweets', TweetViewSet, basename='tweet')
router.register(r'profiles', UserProfileViewSet)
router.register(r'tweets', TweetViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
