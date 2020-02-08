from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from touristspots import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'touristspots', views.TouristSpotViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'comments', views.TouristSpotCommentsViewSet)
router.register(r'favorites', views.FavoriteTouristSpotViewSet)

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
    path('', include(router.urls)),
]
