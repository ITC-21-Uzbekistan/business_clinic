from apps.enrollment.models import Enrollment
from rest_framework import serializers


class EnrollmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
