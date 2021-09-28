from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from utils import log
from utils.response import APIResponse
from .serializer.login_serializer import LoginSerializer
from .models import UserInfo
from rest_framework.exceptions import APIException
# Create your views here.


logging = log.get_logger()


class LoginView(ViewSet):
    @action(methods=['POST'], detail=False)
    def login(self, request):
        ser = LoginSerializer(data=request.data)

        if ser.is_valid(raise_exception=True):
            token = ser.context.get('token')
            username = ser.context.get('username')
            return APIResponse(username=username, token=token)
        else:
            return APIResponse(code=100, msg='Failed')


class CheckMobileView(ViewSet):
    @action(methods=['POST'], detail=False)
    def mobile(self, request):
        mobile = request.POST.get('mobile')
        try:
            UserInfo.objects.get(mobile=mobile)

        except Exception:
            raise APIException('手机号不存在')

        return APIResponse(is_exisit=True)

