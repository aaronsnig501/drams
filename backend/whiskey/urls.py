from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, WhiskeyViewSet

app_name = "whiskey"

router = DefaultRouter()

router.register("", WhiskeyViewSet, basename="whiskey")
router.register("brands", BrandViewSet, basename="brands")

urlpatterns = router.urls
