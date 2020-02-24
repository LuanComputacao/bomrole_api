from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api.views.category import CategoryViewSet
from api.views.comments import TouristSpotCommentsViewSet
from api.views.favorites import FavoriteTouristSpotViewSet
from api.views.pictures import TouristSpotsPicturesViewSet
from api.views.tourist_spots import TouristSpotViewSet, TouristSpotsNear
from api.views.upvotes import TouristSpotUpvotesViewSet
from api.views.users import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'touristspots', TouristSpotViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', TouristSpotCommentsViewSet)
router.register(r'favorites', FavoriteTouristSpotViewSet)
router.register(r'pictures', TouristSpotsPicturesViewSet)
router.register(r'upvotes', TouristSpotUpvotesViewSet)

urlpatterns = [
    url(r'api/touristspots/(?P<pk>[0-9]+)/near/(?P<meters>[0-9]+)/?$', TouristSpotsNear.as_view()),
    path('openapi/',
         get_schema_view(title="Tourist Spots", description="API for the project Tourist Spots", version="1.0.0"),
         name='openapi-schema'),
    path('swagger-ui/',
         TemplateView.as_view(template_name='swagger-ui.html', extra_context={'schema_url': 'openapi-schema'}),
         name='swagger-ui'),
    path('api/', include(router.urls)),
]
