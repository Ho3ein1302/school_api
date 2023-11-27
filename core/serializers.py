from rest_framework import serializers

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from . import models


class SchoolSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = models.School
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'


class HomeRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HomeRoom
        fields = '__all__'
