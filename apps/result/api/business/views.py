from apps.result.models import Result, Result_Files
from apps.result.serializers.serializers import ResultSerializers, ResultFilesSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateResultAPIView(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RetrieveUpdateDestroyResultAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ListCreateResultFilesAPIView(ListCreateAPIView):
    queryset = Result_Files.objects.all()
    serializer_class = ResultFilesSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RetrieveUpdateDestroyResultFilesAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Result_Files.objects.all()
    serializer_class = ResultFilesSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
