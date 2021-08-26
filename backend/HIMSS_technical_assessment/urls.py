"""
HIMSS_technical_assessment URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'reports', views.ReportView)
router.register(r'reports_open', views.ReportOpenView)
router.register(r'references', views.ReferenceView)
router.register(r'payloads', views.PayloadView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]