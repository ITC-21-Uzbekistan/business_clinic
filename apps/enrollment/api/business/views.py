from apps.enrollment.models import Enrollment
from apps.enrollment.serializers.serializers import EnrollmentSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateEnrollmentAPIView(ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RetrieveUpdateDestroyEnrollmentAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
