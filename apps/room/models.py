import uuid

from django.db import models

from apps.direction.models import DirectionMedicine


class Room(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    room_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    direction = models.ForeignKey(
        DirectionMedicine,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'room'
