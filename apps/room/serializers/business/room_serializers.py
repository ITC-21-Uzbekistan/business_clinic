from rest_framework.serializers import ModelSerializer
from apps.room.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
