from rest_framework.generics import ListCreateAPIView, \
                                    RetrieveUpdateDestroyAPIView
from apps.room.models import Room
from apps.room.serializers.business.room_serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateRoomAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RetrieveUpdateDestroyRoomAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
