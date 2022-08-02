from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.accounting.models import Accounting
from apps.accounting.serializers.business import AccountingSerializer


class AccountingListCreateAPIView(ListCreateAPIView):
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AccountingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
