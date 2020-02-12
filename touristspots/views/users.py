from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from touristspots.permissions import IsOwnerOrReadOnly, IsMySelf
from touristspots.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsMySelf]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
