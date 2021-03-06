from rest_framework import viewsets, permissions

from api.models import TouristSpotCategory
from api.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed and edited
    """
    queryset = TouristSpotCategory.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
