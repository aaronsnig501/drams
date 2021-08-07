from django.urls import path
from .views import RegisterAccount

app_name = "accounts"

urlpatterns = [
    path("create/", RegisterAccount.as_view(), name="regsiter_account")
]