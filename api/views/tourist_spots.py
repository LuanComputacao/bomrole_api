import django_filters
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.views import generic
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView

from api.models import TouristSpot
from api.permissions import IsOwnerOrReadOnly
from api.serializers import TouristSpotSerializer


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


class TouristSpotsNear(ListAPIView):
    serializer_class = TouristSpotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        meters = float(self.kwargs['meters'])
        ts = TouristSpot.objects.filter(id=self.kwargs['pk']).first()
        return None if not ts \
            else TouristSpot.objects.filter(point__distance_lte=(ts.point, meters))
