from rest_framework.serializers import ModelSerializer

from apps.accounting.models import Accounting


class AccountingSerializer(ModelSerializer):
    class Meta:
        model = Accounting
        fields = (
            'id',
            'service',
            'account_date',
            'total_amount',
        )
