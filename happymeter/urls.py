"""
URL configuration for happymeter project
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("reports.routes")),
    path("api/", include("members.routes")),
]
