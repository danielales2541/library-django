"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include
from books.api.router import books_router
from Users.api.router import router_users
from loans.api.router import loans_router
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="API Library Django",
      default_version='v1',
      description="Documentación de la API del sistema de biblioteca",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="danielalejandrolara573@gmail.com"),
      license=openapi.License(name="MIT License"),  # opcional
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   url='http://127.0.0.1:8000',  # ✅ Esta línea debe ir aquí
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(books_router.urls)),
    path('api/', include(router_users.urls)),
    path('api/', include(loans_router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Redoc UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
