import uuid

from django.db import models
from apps.service.models import Service
from auth_user.models import User


class Enrollment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    patient_id = models.UUIDField(
        null=True,
        blank=True
    )

    enrollment_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    enrollment_number = models.IntegerField(
        null=True,
        blank=True
    )

    finished = models.BooleanField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'enrollment'


