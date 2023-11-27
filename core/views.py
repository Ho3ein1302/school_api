from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from . import serializers, models


class SchoolView(ListCreateAPIView):
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer


class SchoolDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer


class CourseView(ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class HomeRoomView(ListCreateAPIView):
    queryset = models.HomeRoom.objects.all()
    serializer_class = serializers.HomeRoomSerializer


class HomeRoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.HomeRoom.objects.all()
    serializer_class = serializers.HomeRoomSerializer
