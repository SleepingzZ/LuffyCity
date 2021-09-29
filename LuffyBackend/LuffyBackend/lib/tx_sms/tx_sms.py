import random

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from .settings import *


def get_code():
    code = '{x:0>6}'.format(x=random.randint(0, 999999))
    return code


def send_sms(mobile, code):
    sender = SmsSingleSender(APPID, APPKEY)
    # 模板所需参数，和申请的模板中占位符要保持一致
    params = [code, 5]
    try:
        result = sender.send_with_param(86, mobile, TEMPLATE_ID, params, sign=SMS_SIGN, extend="", ext="")
        return result
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(get_code())
