from rest_framework.routers import DefaultRouter
from .views import PostViewset

app_name = "blog"

router = DefaultRouter()
router.register("", PostViewset, basename="post")
urlpatterns = router.urls
