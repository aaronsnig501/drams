from datetime import datetime
from django.db import models


class Brand(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    year_established = models.IntegerField(
        null=False, blank=False)

    def __str__(self):
        return f"{self.name}"