from datetime import datetime

from core.models import Company, Device, Measurement
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    def create(self, validated_data):
        return Device.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.company = validated_data.get('company', instance.company)
        instance.device_id = validated_data.get('device_id', instance.device_id)
        instance.active = validated_data.get('active', instance.active)
        instance.labels = validated_data.get('labels', instance.labels)
        instance.save()
        return instance


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(value.timestamp())

    def to_internal_value(self, value):
        return datetime.fromtimestamp(value)


class MeasurementSerializer(serializers.ModelSerializer):
    date = TimestampField()

    class Meta:
        model = Measurement
        fields = '__all__'

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)

    def validate_data(self, value):
        valid_keys = {"temperature", "rssi", "humidity"}
        if not value.keys() == valid_keys:
            raise serializers.ValidationError("Bad input: missing keys in data.")

        temperature, rssi, humidity = value["temperature"], value["rssi"], value["humidity"]
        if (
            not isinstance(temperature, float) or not 20 <= temperature <= 38
            or not isinstance(rssi, int) or not 0 <= rssi <= 45
            or not isinstance(humidity, float) or not 0 <= humidity <= 100
        ):
            raise serializers.ValidationError("Bad input: data value(s) invalid.")

        return value