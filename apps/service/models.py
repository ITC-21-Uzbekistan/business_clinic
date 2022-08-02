import uuid

from django.db import models

from apps.direction.models import DirectionMedicine


class Service(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    direction = models.ForeignKey(
        DirectionMedicine,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    price = models.FloatField(
        default=0,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'service'
        ordering = ['id']

    def __str__(self):
        return self.name
