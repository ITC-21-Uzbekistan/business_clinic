from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.category_employee import CategoryEmployee
from apps.category_employee.serializers.business import CategoryEmployeeSerializer


class CategoryEmployeeListCreateAPIView(ListCreateAPIView):
    queryset = CategoryEmployee.objects.all()
    serializer_class = CategoryEmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryEmployeeRetrieveUpdateDestroyAPIView(ListCreateAPIView):
    queryset = CategoryEmployee.objects.all()
    serializer_class = CategoryEmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
