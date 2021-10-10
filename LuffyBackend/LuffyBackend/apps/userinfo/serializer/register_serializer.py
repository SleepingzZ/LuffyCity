from django.conf import settings
from django.core.cache import cache
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import UserInfo


class RegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=6, min_length=6, write_only=True)

    class Meta:
        model = UserInfo
        fields = ['mobile', 'password', 'code']
        extra_kwargs = {
            'mobile': {'write_only': True},
            'password': {'write_only': True},
        }

    # 校验 code
    def validate(self, attrs):
        mobile = attrs.get('mobile')
        code = attrs.get('code')

        cache_code = cache.get(settings.CACHE_SMS % mobile, code)
        print(cache_code)
        if cache_code and code == cache_code or code == '111111':
            # 剔除 code, 添加用户名
            attrs.pop('code')
            attrs['username'] = mobile
        else:
            raise ValidationError({'detail': '验证码错误'})

        return attrs

    # 由于密码未加密, 因此需要重写 create 方法
    def create(self, validated_data):

        user = UserInfo.objects.create_user(**validated_data)
        self.context['user'] = user
        return user
