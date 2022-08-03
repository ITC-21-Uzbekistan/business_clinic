from rest_framework.serializers import ModelSerializer
from apps.schedule.models import Schedule


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            'start_time',
            'finish_time',
            'start_lunch',
            'finish_lunch',
        )
