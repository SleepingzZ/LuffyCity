import random

from qcloudsms_py import SmsSingleSender
from qcloudsms_py import SmsStatusPuller
from qcloudsms_py.httpclient import HTTPError

# 申请的短信应用 SDK AppID
appid = 1400578647
# 申请的短信应用 SDK AppKey
appkey = "d8f525469bfd222500ba06337983ed20"
# 申请的短信模板ID，需要在短信控制台中申请
template_id = 1139351
# 申请的签名，参数使用的是`签名内容`，而不是`签名ID`
sms_sign = "SleepingzZ"

sender = SmsSingleSender(appid, appkey)


def get_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


mobile = 18658025230
# 模板所需参数，和申请的模板中占位符要保持一致
code = get_code()
print(code)
params = [code, 3]
try:
    result = sender.send_with_param(86, mobile, template_id, params, sign=sms_sign, extend="", ext="")
    if result and result.get('result') == 0:
        print('发送成功')
except Exception as e:
    print('短信发送失败：%s' % e)
#
# max_num = 10  # 单次拉取最大量
# spuller = SmsStatusPuller(appid, appkey)
# try:
#     # 拉取短信回执
#     callback_result = spuller.pull_callback(max_num)
#     # 拉取回复（国际/港澳台短信不支持回复功能）
#     reply_result = spuller.pull_reply(max_num)
# except HTTPError as e:
#     print(e)
# except Exception as e:
#     print(e)
# print(callback_result)
# print(reply_result)
