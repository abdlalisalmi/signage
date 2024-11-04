from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, "404.html", status=404)


handler404 = custom_404_view

API_VERSION = "v1"
API_PREFIX = f"api/{API_VERSION}/"


urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{API_PREFIX}", include("signage.urls")),
    path("", include("frontend.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
