from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .users.views import UserViewSet, UserCreateViewSet
from .firmware.views import FirmwareViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'firmware', FirmwareViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Versionator API",
        default_version='v1',
        description="Application created to manage firmware versioning",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sdavidlevy@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('signin/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
