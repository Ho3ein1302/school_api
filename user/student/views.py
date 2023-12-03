from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from core.permissions import CustomModelPermissions, IsUser
from core import models
from user.models import User


class StudentRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.StudentRegisterSerializer


class StudentProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsUser]
    queryset = User.objects.all()
    serializer_class = serializers.StudentProfileSerializer


class StudentClassView(GenericAPIView):
    serializer_class = serializers.StudentHomeRoomSerializer

    def get(self, request: Request):
        try:
            user = request.user
            homeroom = models.HomeRoom.objects.filter(students=user)
            s_homeroom = self.serializer_class(instance=homeroom, many=True)
            return Response(s_homeroom.data, status.HTTP_200_OK)
        except:
            return Response({'msg': 'Token invalid'}, status.HTTP_400_BAD_REQUEST)


class StudentNewsView(GenericAPIView):
    serializer_class = serializers.StudentNewsSerializer

    def get(self, request: Request):
        try:
            user = request.user
            homeroom = models.HomeRoom.objects.filter(students=user)
            news = models.News.objects.filter(class_id__in=homeroom)
            s_news = self.serializer_class(instance=news, many=True)
            return Response(s_news.data, status.HTTP_200_OK)
        except:
            return Response({'msg': 'Token invalid'}, status.HTTP_400_BAD_REQUEST)


class DetailNewsView(RetrieveAPIView):
    permission_classes = [CustomModelPermissions]
    queryset = models.News.objects.all()
    serializer_class = serializers.StudentNewsSerializer


class StudentHomeworkView(GenericAPIView):
    serializer_class = serializers.StudentHomeworkSerializer

    def get(self, request: Request):
        try:
            user = request.user
            homeroom = models.HomeRoom.objects.filter(students=user)
            practice = models.HomeWork.objects.filter(class_id__in=homeroom)
            s_practice = self.serializer_class(instance=practice, many=True)
            return Response(s_practice.data, status.HTTP_200_OK)
        except:
            return Response({'msg': 'Token invalid'}, status.HTTP_400_BAD_REQUEST)


class DetailHomeWorkView(RetrieveAPIView):
    permission_classes = [CustomModelPermissions]
    queryset = models.HomeWork.objects.all()
    serializer_class = serializers.StudentHomeworkSerializer


class StudentHomeWorkResponseView(CreateAPIView):
    permission_classes = [CustomModelPermissions]
    queryset = models.HomeWorkResponse.objects.all()
    serializer_class = serializers.StudentHomeWorkResponseSerializer


class DetailStudentHomeWorkResponseView(RetrieveUpdateAPIView):
    permission_classes = [CustomModelPermissions]
    queryset = models.HomeWorkResponse.objects.all()
    serializer_class = serializers.StudentHomeWorkResponseSerializer
