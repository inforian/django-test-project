"""
version v1 router
"""
from django.urls import path, include



urlpatterns = [
    path(r"", include("hangry_app.routers_v1")),
]
