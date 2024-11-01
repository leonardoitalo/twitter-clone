from rest_framework.routers import DefaultRouter
from tweets.views import UserProfileViewSet, TweetViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'tweets', TweetViewSet)

urlpatterns = router.urls
