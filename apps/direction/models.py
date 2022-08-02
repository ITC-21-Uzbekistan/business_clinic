import uuid

from django.db import models


class DirectionMedicine(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'direction_medicine'
        ordering = ['id']
