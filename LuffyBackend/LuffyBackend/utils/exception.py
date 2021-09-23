from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import exception_handler as drf_exception_handler

import logging
from utils.log import logger

logging.getLogger()


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    if response is None:  # drf没有处理的，django的异常
        # response = Response({'detail': '服务器异常，请重试...'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response = Response({'code': 999, 'msg': '服务器异常，请重试...'})
    else:
        response = Response({'code': 998, 'msg': response.data['detail']})
    # 记录服务器异常,drf和django的异常，都记录
    logger.critical('%s' % exc)
    return response
