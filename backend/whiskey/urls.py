from rest_framework.routers import DefaultRouter
from .views import BrandViewSet

app_name = "whiskey"

router = DefaultRouter()
router.register("brands", BrandViewSet, basename="brands")
urlpatterns = router.urls
