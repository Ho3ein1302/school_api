from django.utils.translation import gettext as _

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class UserLoginView(GenericAPIView):
    serializer_class = serializers.UserLoginSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)


class UserLogoutView(GenericAPIView):
    serializer_class = serializers.UserLogoutSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': _('logout OK.')}, status.HTTP_200_OK)


class RefreshTokenView(GenericAPIView):
    serializer_class = serializers.RefreshTokenSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)