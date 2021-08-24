from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Brand, Whiskey
from .serializers import BrandSerializer, WhiskeySerializer


class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Brand, id=item)

    def get_queryset(self):
        return Brand.objects.all()


class WhiskeyViewSet(ModelViewSet):
    serializer_class = WhiskeySerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Whiskey, id=item)

    def get_queryset(self):
        return Whiskey.objects.all()