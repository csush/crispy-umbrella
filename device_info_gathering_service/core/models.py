import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(
        verbose_name=_('UUID'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        verbose_name=_('Updated at'),
        auto_now=True,
    )

    class Meta:
        abstract = True


class Company(BaseModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        unique=True,
    )

    location = models.CharField(
        verbose_name=_('Location'),
        max_length=100,
    )
