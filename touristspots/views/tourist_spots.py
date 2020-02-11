import django_filters
from rest_framework import viewsets, permissions

from touristspots.models import TouristSpot
from touristspots.permissions import IsOwnerOrReadOnly
from touristspots.serializers import TouristSpotSerializer


class TouristSpotFilter(django_filters.FilterSet):
    """
    Filter to be applied to the Tourist Spot View Set
    """

    class Meta:
        model = TouristSpot
        fields = {
            'name': ['icontains']
        }


class TouristSpotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourist Spots to be viewed and edited
    """
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    filterset_class = TouristSpotFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(registered_by=self.request.user)
