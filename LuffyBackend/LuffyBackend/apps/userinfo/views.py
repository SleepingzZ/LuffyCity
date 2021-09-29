import re

from django.conf import settings
from django.core.cache import cache
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin

from lib.tx_sms import tx_sms
from utils import log
from utils.response import APIResponse
from utils.throttle import SMSThrottle
from .models import UserInfo
from .serializer.login_serializer import LoginSerializer
from .serializer.mobile_login_serializer import MobileLoginSerializer
from .serializer.register_serializer import RegisterSerializer

# Create your views here.


logging = log.get_logger()


class LoginView(ViewSet):
    # 用户名登录
    @action(methods=['POST'], detail=False)
    def login(self, request):
        ser = LoginSerializer(data=request.data)

        ser.is_valid(raise_exception=True)
        token = ser.context.get('token')
        username = ser.context.get('username')
        return APIResponse(username=username, token=token)

    # 手机验证码登录
    @action(methods=['POST'], detail=False, url_path='mlogin')
    def mobile_login(self, request):
        ser = MobileLoginSerializer(data=request.data)

        ser.is_valid(raise_exception=True)
        token = ser.context.get('token')
        username = ser.context.get('username')
        return APIResponse(username=username, token=token)

    # 获取验证码, 并限制频率
    @action(methods=['GET'], detail=False, url_path='sms', throttle_classes=[SMSThrottle])
    def send_sms(self, request):
        mobile = request.query_params.get('mobile')

        if mobile and re.match(r'^1[3-9][0-9]{9}$', mobile):
            code = tx_sms.get_code()

            # 将验证码存入缓存
            cache.set(settings.CACHE_SMS % mobile, code)

            res = tx_sms.send_sms(mobile, code)
            if res:
                return APIResponse(mobile=mobile, code=code)
            else:
                raise APIException('短信发送失败')
        else:
            raise APIException('手机号不合法')


class CheckMobileView(ViewSet):
    @action(methods=['POST'], detail=False)
    def mobile(self, request):
        mobile = request.POST.get('mobile')
        try:
            UserInfo.objects.get(mobile=mobile)

        except Exception:
            raise APIException('手机号不存在')

        return APIResponse(is_exisit=True)


class RegisterView(GenericViewSet, CreateModelMixin):
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return APIResponse(**response.data)
