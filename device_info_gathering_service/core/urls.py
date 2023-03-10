from core import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='company')
router.register(r'devices', views.DeviceViewSet, basename='device')
router.register(r'measurements', views.MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('', include(router.urls)),
]
