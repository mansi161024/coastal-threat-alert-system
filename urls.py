from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .models import SafeZone, Alert

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ API routes from alerts app
    path('api/', include('alerts.urls')),

    # ✅ DRF login/logout (useful for testing in browsable API)
    path('api-auth/', include('rest_framework.urls')),
]

# ✅ Serve media files in development (uploads like images, voices)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)