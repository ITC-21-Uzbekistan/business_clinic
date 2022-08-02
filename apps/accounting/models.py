import uuid

from django.db import models

from apps.service.models import Service


class Accounting(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    account_date = models.DateField(
        default=None,
        blank=True,
        null=True
    )

    total_amount = models.FloatField(
        default=0,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'accounting'
        ordering = ['id']

    def __str__(self):
        return self.service.name
