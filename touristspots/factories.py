import factory
from factory.django import DjangoModelFactory

from touristspots.models import TouristSpot


class TouristSpotFactory(DjangoModelFactory):
    class Meta:
        model = TouristSpot
