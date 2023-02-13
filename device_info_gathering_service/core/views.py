from datetime import datetime

from core.models import Company, Device, Measurement
from core.serializers import CompanySerializer, DeviceSerializer, MeasurementSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        queryset = Device.objects.all()
        company = self.request.query_params.get('company')
        if company is not None:
            queryset = queryset.filter(company__pk=company)
        labels = self.request.query_params.getlist('labels[]')
        if labels is not None:
            queryset = queryset.filter(labels__contains=labels)
        return queryset


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        queryset = Measurement.objects.all()

        device = self.request.query_params.get('device')
        if device is not None:
            queryset = queryset.filter(device__pk=device)

        company = self.request.query_params.get('company')
        if company is not None:
            queryset = queryset.filter(device__company__pk=company)

        datetime_start = datetime.fromtimestamp(int(self.request.query_params.get("datetime_start", 0)))
        datetime_end = datetime.fromtimestamp(int(self.request.query_params.get("datetime_end", 4831922865))) # arbitrary high timestamp
        queryset = queryset.filter(date__range=(datetime_start, datetime_end))

        return queryset

    @action(detail=False, methods=["get"])
    def averagetemp(self, request, **kwargs):
        queryset = self.get_queryset()
        if queryset.count() > 0:
            sum = 0
            for q in queryset:
                sum += q.data["temperature"]
            average_temp = sum / queryset.count()
            return Response(average_temp)
        
        return Response(data=None)