import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from userinfo.models import UserInfo


class LoginSerializer(serializers.ModelSerializer):
    """
    username 由于映射了 UserInfo 的 username, 且 unique=True, 即 username 本身的校验规则会走 unique=True,
    回去数据亏查询是否已经有这个用户, 如果有则直接抛异常, 因此需要重写该字段, 不设规则
    """
    username = serializers.CharField(max_length=16, min_length=4)

    class Meta:
        model = UserInfo
        fields = ['username', 'password']

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
        username = attrs.get('username')
        password = attrs.get('password')
        # 多方式登录
        if re.match(r'^1[3-9][0-9]{9}$', username):
            user = UserInfo.objects.filter(mobile=username).first()

        else:
            user = UserInfo.objects.filter(username=username).first()

        if user and user.check_password(password):
            return user

        else:
            raise ValidationError({'detail': '用户名或密码错误'})

    def _get_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token
