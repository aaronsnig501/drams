from rest_framework.serializers import (
    ModelSerializer, CharField, IntegerField, StringRelatedField, ValidationError)
from rest_framework.validators import UniqueValidator
from .models import Brand, Whiskey


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "year_established", "type", "region")

    name = CharField(
        max_length=50, validators=[UniqueValidator(queryset=Brand.objects.all())])
    year_established = IntegerField()

    def validate_year_established(self, value):
        if len(str(value)) != 4:
            raise ValidationError("Year must contain 4 digits")
        return value


class WhiskeySerializer(ModelSerializer):

    class Meta:
        model = Whiskey
        fields = (
            "id",
            "name",
            "brand",
            "age_statement",
            "colour",
            "chill_filtered",
            "description",
            "image",
            "proof",
            "abv"
        )

    brand = StringRelatedField()