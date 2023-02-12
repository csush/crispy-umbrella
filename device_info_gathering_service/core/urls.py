from core import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('companies/<str:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)