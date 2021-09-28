from utils import log
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from utils import log
from utils.response import APIResponse
from .serializer.login_serializer import LoginSerializer

# Create your views here.


logging = log.get_logger()

#
# class LoginView(ViewSet):
#     @action(methods='POST', detail=False)
#     def login(self, request):
#         ser = LoginSerializer(data=request.data)
#
#         if ser.is_valid():
#             pass
#         else:
#             return APIResponse(code=100, msg='Failed')
