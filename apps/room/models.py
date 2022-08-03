import uuid
from django.db import models
from apps.direction.models import DirectionMedicine

class Room(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    room_namber = models.PositiveIntegerField(null=True, blank=True)
    direction = models.ForeignKey(DirectionMedicine, on_delete=models.CASCADE())
