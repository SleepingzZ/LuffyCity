from django.conf import settings
from django.core.cache import cache
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from ..models import UserInfo


class MobileLoginSerializer(serializers.ModelSerializer):
    """
    username 由于映射了 UserInfo 的 username, 且 unique=True, 即 username 本身的校验规则会走 unique=True,
    回去数据亏查询是否已经有这个用户, 如果有则直接抛异常, 因此需要重写该字段, 不设规则
    """
    mobile = serializers.CharField()  # 重写 mobile 字段, 是由于 unique=True
    code = serializers.CharField()  # 表中没有 code 字段,因此需要重写

    class Meta:
        model = UserInfo
        fields = ['mobile', 'code']

    def validate(self, attrs):
        """
        1、根据用户名获取用户
        2、用户存在签发 token
        3、把 token 放到序列化类的对象中
        """
        user = self._get_user(attrs)
        token = self._get_token(user)
        self.context['token'] = token
        self.context['username'] = user.username
        return attrs

    # 不是隐藏方法, 伪私有方法, 一般只供公司内部使用, 外部也可以调用
    def _get_user(self, attrs):
        mobile = attrs.get('mobile')
        code = attrs.get('code')

        # 获取缓存中的验证码
        cache_code = cache.get(settings.CACHE_SMS % mobile)

        # 校验验证码
        if cache_code and code == cache_code:
            # 校验结束, 验证码置为空
            cache.set(settings.CACHE_SMS % mobile, '')
            user = UserInfo.objects.filter(mobile=mobile).first()

            if user:
                return user
            else:
                raise ValidationError({'detail': '用户名或密码错误'})

        else:
            raise ValidationError({'detail': '验证码错误'})

    def _get_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token
