from datetime import datetime
from django.db.models import Model, CharField, IntegerField, ForeignKey, RESTRICT
from django_countries.fields import CountryField


class Region(Model):

    name = CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Type(Model):

    name = CharField(max_length=25, null=False, blank=False)
    country = CountryField(blank_label="Select country")

    def __str__(self):
        return f"{self.name}"


class Brand(Model):

    name = CharField(max_length=50, null=False, blank=False)
    year_established = IntegerField(null=False, blank=False)
    type = ForeignKey(Type, related_name="type", on_delete=RESTRICT)
    region = ForeignKey(
        Region, null=True, blank=True, related_name="region", on_delete=RESTRICT)

    def __str__(self):
        return f"{self.name}"