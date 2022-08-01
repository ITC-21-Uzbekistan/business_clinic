from rest_framework.serializers import ModelSerializer

from apps.direction import DirectionMedicine


class DirectionMedicineSerializer(ModelSerializer):
    class Meta:
        model = DirectionMedicine
        fields = (
            'id',
            'name',
        )
