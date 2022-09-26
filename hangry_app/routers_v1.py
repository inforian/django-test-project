"""
Hangry App versionv1 router
"""
from django.urls import path
from rest_framework.routers import SimpleRouter

from hangry_app.views import HangryPersonViewSet

router = SimpleRouter()

router.register(
    "persons",
    HangryPersonViewSet,
    basename="hangry-person-v1",
)


urlpatterns = [
]

urlpatterns += router.urls
