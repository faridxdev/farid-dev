from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from api.views import ProjectViewSet, ArticleViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='api-projects')
router.register('articles', ArticleViewSet, basename='api-articles')

schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio API",
        default_version='v1',
        description="API REST du portfolio backend developer",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('api/v1/', include(router.urls)),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='api-redoc'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)