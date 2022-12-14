from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from auth_user.models import User
from auth_user.serializers import UserSerializer


def get_tokens_to_users(user):
    refresh = RefreshToken.for_user(user=user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class SingUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(operation_summary="Ro'yhatdan o'tish")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlacklistRefreshView(APIView):
    @transaction.atomic
    @swagger_auto_schema(operation_summary="Hisobdan chiqish")
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success", status=status.HTTP_200_OK)
