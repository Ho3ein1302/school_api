from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth.models import Group

from rest_framework import serializers

from user.models import User
from core.utils import get_tokens
from user.serializers import GroupSerializer
from core import models


class TeacherRegisterSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(
        min_length=8,
        label=_('confirm password'),
        write_only=True,
        required=True
    )
    groups = GroupSerializer(
        many=True,
        read_only=True
    )
    token = serializers.SerializerMethodField(
        read_only=True,
        label=_('token')
    )

    class Meta:
        model = User
        fields = [
            'code_meli',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'password',
            're_password',
            'groups',
            'token',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'read_only': True},
        }

    def validate(self, data):
        password = data.get('password')
        re_paasword = data.get('re_paasword')
        if password != re_paasword:
            raise ValidationError(_('The passwords must match'))
        return data

    def get_token(self, obj):
        user = User.objects.get(code_meli=obj.code_meli)
        token = get_tokens(user)
        refresh = token['refresh']
        access = token['access']
        settings.REDIS_JWT_TOKEN.set(
            name=refresh,
            value=refresh,
            ex=settings.REDIS_REFRESH_TIME
        )
        return {'access': access, 'refresh': refresh}

    def create(self, validated_data):
        user = User.objects.create(
            code_meli=validated_data['code_meli'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
        )
        group = Group.objects.get(name='معلم')
        group.user_set.add(user)
        return user


class TeacherProfileSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'code_meli',
            'bio'
            'groups',
        ]


class HomeRoomAddStudentSerializer(serializers.ModelSerializer):
    code_meli = serializers.CharField(
        required=True,
        label=_('code meli'),
        write_only=True
    )

    class Meta:
        model = models.HomeRoom
        fields = [
            'id',
            'code_meli'
        ]

    def validate_code_meli(self, data):
        try:
            User.objects.get(code_meli=data)
            return data
        except User.DoesNotExist:
            raise ValidationError(_('invalid code meli.'))

    def update(self, instance, validated_data):
        try:
            student = User.objects.get(code_meli=validated_data['code_meli'])
            homeroom = instance
            homeroom.students.add(student)
            homeroom.save()
            return instance
        except:
            raise ValidationError(_('invalid code meli.'))


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeWork
        fields = '__all__'
