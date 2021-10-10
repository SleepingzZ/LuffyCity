
from .celery import work


@work.task()
def sms(x):
    x += 1
    return True
