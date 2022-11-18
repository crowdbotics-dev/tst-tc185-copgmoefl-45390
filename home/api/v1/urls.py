from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AddresspdzbhyfwcsViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('addresspdzbhyfwcs', AddresspdzbhyfwcsViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
