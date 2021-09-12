from datetime import datetime
from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    TextField,
    ImageField,
    DateTimeField,
    RESTRICT
)
from django_countries.fields import CountryField
from accounts.models import Account


class Region(Model):
    """Region table

    The whisky regions. For now this will likely only be used for scotch regions
    """

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
    region = ForeignKey(
        Region, null=True, blank=True, related_name="region", on_delete=RESTRICT
    )

    def __str__(self):
        return f"{self.name}"


class Whiskey(Model):

    COLOURING = [
        ("0", "Unknown"),
        ("1", "Coloured"),
        ("2", "Natural"),
    ]

    CHILL_FILTERED = [
        ("0", "Unknown"),
        ("1", "Chill-filtered"),
        ("2", "Non-chill-filtered")
    ]

    name = CharField(max_length=75, null=False, blank=False)
    brand = ForeignKey(Brand, related_name="brand", on_delete=RESTRICT)
    age_statement = CharField(max_length=3, null=False, blank=False)
    colour = CharField(max_length=1, choices=COLOURING, default="0")
    chill_filtered = CharField(max_length=1, choices=CHILL_FILTERED, default="0")
    description = TextField()
    image = ImageField(upload_to="media/")
    proof = IntegerField()
    type = ForeignKey(Type, related_name="type", on_delete=RESTRICT)
    added_by = ForeignKey(Account, on_delete=RESTRICT)
    created_on = DateTimeField(auto_now_add=True, editable=False)
    last_modified = DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    @property
    def abv(self):
        return f"{self.proof / 2}%"