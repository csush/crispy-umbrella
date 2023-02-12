from core import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
]
