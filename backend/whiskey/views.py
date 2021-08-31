from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .models import Brand, Whiskey
from .serializers import BrandSerializer, WhiskeySerializer


class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Brand, id=item)


class WhiskeyViewSet(ModelViewSet):
    serializer_class = WhiskeySerializer
    queryset = Whiskey.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "brand__name"]

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Whiskey, id=item)
