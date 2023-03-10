from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from config import settings
from django.conf.urls.i18n import i18n_patterns

schema_view = get_schema_view(
    openapi.Info(
        title="Ayol Uchun Backend",
        default_version='v1',
        description="Backend API for Ayol Uchun ",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n"))
]

urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path('api/v1/', include('apps.urls')),
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)