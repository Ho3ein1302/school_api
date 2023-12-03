from django.conf import settings
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from core.utils import get_tokens


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'code_meli',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'groups',
        ]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        label=_('username'),
        write_only=True
    )
    password = serializers.CharField(
        required=True,
        label=_('password'),
        min_length=8,
        write_only=True
    )
    user = serializers.SerializerMethodField(
        read_only=True,
        label=_('user')
    )
    token = serializers.SerializerMethodField(
        read_only=True,
        label=_('user')
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) and user.is_active:
                return data
            raise ValidationError(_('The username or password is not valid'))
        except:
            raise ValidationError(_('The username or password is not valid'))

    def get_user(self, obj):
        try:
            user = User.objects.get(
                username=obj['username']
            )
            user = UserSerializer(
                instance=user
            )
            return user.data
        except:
            raise ValidationError(
                _('The username or password is not valid')
            )

    def get_token(self, obj):
        try:
            user = User.objects.get(
                username=obj['username']
            )
            token = get_tokens(user)
            refresh = token['refresh']
            access = token['access']
            settings.REDIS_JWT_TOKEN.set(
                name=refresh,
                value=refresh,
                ex=settings.REDIS_REFRESH_TIME
            )
            return {'access': access, 'refresh': refresh}
        except:
            raise ValidationError(
                _('The username or password is not valid')
            )


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        max_length=1000,
        required=True,
        label=_('refresh')
    )

    def validate_refresh(self, data):
        if settings.REDIS_JWT_TOKEN.get(name=data):
            settings.REDIS_JWT_TOKEN.delete(data)
            return data
        else:
            raise ValidationError(
                _('Token is invalid or expired')
            )


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        max_length=1000,
        required=True,
        label=_('refresh'),
        write_only=True
    )
    token = serializers.SerializerMethodField(
        read_only=True,
        label=_('token')
    )

    def validate_refresh(self, data):
        if settings.REDIS_JWT_TOKEN.get(name=data):
            return data
        else:
            raise ValidationError(
                _('Token is invalid or expired')
            )

    def get_token(self, obj):
        refresh = settings.REDIS_JWT_TOKEN.get(name=obj['refresh'])
        token_refresh = RefreshToken(refresh)
        user = User.objects.get(id=token_refresh['user_id'])
        settings.REDIS_JWT_TOKEN.delete(refresh)
        token = get_tokens(user)
        access = token['access']
        refresh = token['refresh']
        settings.REDIS_JWT_TOKEN.set(name=refresh, value=refresh, ex=settings.REDIS_REFRESH_TIME)
        data = {'access': access, 'refresh': refresh}
        return data
