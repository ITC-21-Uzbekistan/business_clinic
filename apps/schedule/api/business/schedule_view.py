from rest_framework.generics import ListCreateAPIView, \
                                    RetrieveUpdateDestroyAPIView
from apps.schedule.serializers.business.schedule_serializers import ScheduleSerializer
from apps.schedule.models import Schedule
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ListCreateScheduleAPIView(ListCreateAPIView):
    queryset = Schedule.object.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class RetrieveUpdateDestroyScheduleAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Schedule.object.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)