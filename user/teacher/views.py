from django.utils.translation import gettext as _
from rest_framework import status

from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from core.permissions import CustomModelPermissions, IsOwner, IsUser, IsTeacher
from . import serializers
from user.models import User
from core import models


class TeacherRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.TeacherRegisterSerializer


class TeacherProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsUser]
    queryset = User.objects.all()
    serializer_class = serializers.TeacherProfileSerializer


class HomeRoomAddStudentView(UpdateAPIView):
    permission_classes = [CustomModelPermissions, IsTeacher]
    queryset = models.HomeRoom.objects.all()
    serializer_class = serializers.HomeRoomAddStudentSerializer

    def update(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(
            instance=self.get_object(),
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': _('student add to class.')}, status.HTTP_200_OK)


class NewsView(CreateAPIView):
    permission_classes = [CustomModelPermissions]
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsUpdateView(RetrieveUpdateAPIView):
    permission_classes = [CustomModelPermissions, IsOwner]
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class HomeWorkView(CreateAPIView):
    permission_classes = [CustomModelPermissions]
    queryset = models.HomeWork.objects.all()
    serializer_class = serializers.HomeWorkSerializer


class HomeworkUpdateView(RetrieveUpdateAPIView):
    permission_classes = [CustomModelPermissions, IsOwner]
    queryset = models.HomeWork.objects.all()
    serializer_class = serializers.HomeWorkSerializer
