import uuid

from django.db import models
from apps.enrollment.models import Enrollment


class ResultFiles(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    result_file = models.FileField(
        upload_to='result_file/',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'result_files'


class Result(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    enrollment = models.OneToOneField(
        Enrollment,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        max_length=200,
        null=True,
        blank=True
    )
    result_files = models.ManyToManyField(
        ResultFiles
    )

    class Meta:
        db_table = 'result'

