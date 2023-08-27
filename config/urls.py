"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.university, name='university')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='university')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, authentication
from urlshortener.views import go as view

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@lamsta.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    authentication_classes=[authentication.TokenAuthentication, ],

)

urlpatterns = [
    path(
        "",
        include("base.urls")),
    path(
        "auth/",
        include("auth_login.urls")),
    path(
        "home/",
        include("home.urls")),
    path(
        settings.ADMIN_URL,
        admin.site.urls),
    re_path(
        r'swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(
            cache_timeout=0),
        name='schema-json'),
    path(
        r'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0),
        name='schema-swagger-ui'),
    path("urlshortener/", include("urlshortener.urls")),
    path('<str:pk>', view, name='go'),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                   document_root=settings.MEDIA_ROOT)
