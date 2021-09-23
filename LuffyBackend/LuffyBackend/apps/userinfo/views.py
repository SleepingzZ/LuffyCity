from django.shortcuts import render, HttpResponse

# Create your views here.


from utils import log
logging = log.get_logger()


def add(request):
    logging.info('这是日志')
    return HttpResponse('ok')
