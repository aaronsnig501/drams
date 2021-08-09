from django.urls import path
from .views import RegisterAccount, Profile, BlacklistTokenView

app_name = "accounts"

urlpatterns = [
    path("create/", RegisterAccount.as_view(), name="register_account"),
    path("me/", Profile.as_view(), name="profile"),
    path("logout/blacklist/", BlacklistTokenView.as_view(), name="blacklist")
]