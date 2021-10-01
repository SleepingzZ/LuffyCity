import random

from qcloudsms_py import SmsSingleSender

from utils.log import get_logger
from .settings import *

logger = get_logger()


def get_code():
    code = '{x:0>6}'.format(x=random.randint(0, 999999))
    return code


def send_sms(mobile, code):
    sender = SmsSingleSender(APPID, APPKEY)
    # 模板所需参数，和申请的模板中占位符要保持一致
    params = [code, 5]
    try:
        result = sender.send_with_param(86, mobile, TEMPLATE_ID, params, sign=SMS_SIGN, extend="", ext="")

    except Exception as e:
        # 记录日志
        logger.error('%s手机号，发送短信失败，错误信息是%s' % (mobile, str(e)))

    if result['result'] == 0:

        return True

    else:

        logger.warning('%s手机号，发送短信失败,失败原因是%s' % (mobile, result['errmsg']))
        return False


if __name__ == '__main__':
    print(get_code())
