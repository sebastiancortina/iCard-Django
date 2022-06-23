from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Documentacion de la api a iCard",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sebastiancortina97@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
]
