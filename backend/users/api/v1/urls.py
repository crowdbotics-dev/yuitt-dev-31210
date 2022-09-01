from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HjjfjfViewSet

router = DefaultRouter()
router.register("hjjfjf", HjjfjfViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
