from core.models import BaseModel, Company
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ['id', 'created_at', 'updated_at']


class CompanySerializer(BaseSerializer):
    class Meta:
        model = Company
        fields = BaseSerializer.Meta.fields + ['name', 'location']

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
