from apps.result.models import Result, Result_Files
from rest_framework import serializers


class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class ResultFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result_Files
        fields = '__all__'

