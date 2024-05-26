from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from src.django_project.career_app.views import CareerViewSet

router = DefaultRouter()

router.register(r"careers", CareerViewSet, basename="career")


urlpatterns = [path("admin/", admin.site.urls)] + router.urls
