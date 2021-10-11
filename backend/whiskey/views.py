from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Brand, Whiskey
from .serializers import BrandSerializer, WhiskeySerializer
from .pagination import StandardResultsSetPagination


class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Brand, id=item)


class WhiskeyViewSet(ModelViewSet):
    serializer_class = WhiskeySerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "brand__name", "type__name"]
    pagination_class = StandardResultsSetPagination

    def _parse_query_params(self):
        """Parse query params

        Helper method to help parsing any query paramenters that may be provided by the
        UI
        """
        colour_param = None
        chill_filtered_param = None
        params = self.request.GET

        if "colour" in params:
            colour_param = Whiskey.COLOURING[int(params["colour"])][0]

        if "chill_filtered" in params:
            chill_filtered_param = Whiskey.CHILL_FILTERED[int(
                params["chill_filtered"])][0]

        name_param = params.get("name", None)
        proof_param = params.get("proof", None)

        params = {
            "colour": colour_param,
            "chill_filtered": chill_filtered_param,
            "proof": proof_param
        }

        return {k: v for k, v in params.items() if v is not None}

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Whiskey, id=item)

    def get_queryset(self):
        params = self._parse_query_params()
        return Whiskey.objects.all().filter(**params).order_by(
            self.request.GET.get("ordering", "-name"))
