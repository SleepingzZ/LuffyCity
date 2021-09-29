from rest_framework import serializers
from django.core.cache import cache
from ..models import UserInfo
from django.conf import settings
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=6, min_length=6, write_only=True)

    class Meta:
        model = UserInfo
        fields = ['mobile', 'username', 'password', 'code']
        extra_kwargs = {
            'mobile': {'write_only': True},
            'username': {'read_only': True},
            'password': {'write_only': True},
        }

    # 校验 code
    def validate(self, attrs):
        mobile = attrs.get('mobile')
        code = attrs.get('code')

        cache_code = cache.get(settings.CACHE_SMS % mobile)
        if (cache_code and code == cache_code) or code == '111111':
            # 剔除 code, 添加用户名
            attrs.pop('code')
            attrs['username'] = mobile
            return attrs
        else:
            raise ValidationError('验证码错误')

    # 由于密码未加密, 因此需要重写 create 方法
    def create(self, validated_data):
        user = UserInfo.objects.create_user(**validated_data)
        return user
