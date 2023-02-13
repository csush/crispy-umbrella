import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    id = models.UUIDField(
        verbose_name=_('UUID'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)


class Device(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='devices',
        on_delete=models.CASCADE,
    )
    device_id = models.CharField(
        verbose_name=_('Device ID'),
        max_length=50,
        primary_key=True,
    )
    active = models.BooleanField()
    labels = ArrayField(
        models.CharField(max_length=50, null=True, blank=True),
        null=True,
        blank=True,
    )


class Measurement(models.Model):
    date = models.DateTimeField()
    device = models.ForeignKey(
        Device,
        related_name='measurements',
        on_delete=models.CASCADE,
    )
    data = models.JSONField()
