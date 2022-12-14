from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.direction.models import DirectionMedicine
from apps.direction.serializers.business.direction_serializer import DirectionMedicineSerializer


class DirectionMedicineListCreateAPIView(ListCreateAPIView):
    queryset = DirectionMedicine.objects.all()
    serializer_class = DirectionMedicineSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DirectionMedicineRetrieveUpdateDestroyAPIView(ListCreateAPIView):
    queryset = DirectionMedicine.objects.all()
    serializer_class = DirectionMedicineSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
