"""bomrole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('touristspots.urls')),
                  path('api/auth/', include('rest_framework_social_oauth2.urls')),
                  path("logout/", auth_views.LogoutView.as_view(), name="logout"),
                  path(r'^api/login/', include('rest_social_auth.urls_jwt')),
                  path(r'^api/login/', include('rest_social_auth.urls_token')),
                  path(r'^api/login/', include('rest_social_auth.urls_session')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
