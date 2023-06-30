from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        ordering = ["username"]


class Object(models.Model):
    class CategoryChoices(models.TextChoices):
        RESTAURANT = "RESTAURANT"
        HOTEL = "HOTEL"
        CAFE = "CAFE"
        SUPERMARKET = "SUPERMARKET"

    class CityChoices(models.TextChoices):
        KYIV = "KYIV"
        PARIS = "PARIS"
        WARSAW = "WARSAW"
        BERLIN = "BERLIN"
        ROME = "ROME"
        MILAN = "MILAN"
        OSLO = "OSLO"
        PORTO = "PORTO"
        MADRID = "MADRID"
        COPENHAGEN = "COPENHAGEN"

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=63, choices=CityChoices.choices)
    category = models.CharField(max_length=63, choices=CategoryChoices.choices)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return str(self.name)
