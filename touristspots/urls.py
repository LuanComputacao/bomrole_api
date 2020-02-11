from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from touristspots.views.category import CategoryViewSet
from touristspots.views.comments import TouristSpotCommentsViewSet
from touristspots.views.favorites import FavoriteTouristSpotViewSet
from touristspots.views.home import Home, Login
from touristspots.views.pictures import TouristSpotsPicturesViewSet
from touristspots.views.tourist_spots import TouristSpotViewSet
from touristspots.views.users import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'touristspots', TouristSpotViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', TouristSpotCommentsViewSet)
router.register(r'favorites', FavoriteTouristSpotViewSet)
router.register(r'pictures', TouristSpotsPicturesViewSet)

urlpatterns = [
    path('openapi/', get_schema_view(
        title="Tourist Spots",
        description="API for the project Tourist Spots",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('api/', include(router.urls)),
    path("", Home.as_view(), name="home"),
    path("login/", Login.as_view(), name="login")
]
