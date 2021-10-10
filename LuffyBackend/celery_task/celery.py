from celery import Celery
from datetime import timedelta
# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LuffyBackend.settings.dev')
broker = 'redis://127.0.0.1:6379/1'  # redis地址
backend = 'redis://127.0.0.1:6379/2'  # redis地址

# 1 实例化得到celery对象
work = Celery(__name__, backend=backend, broker=broker, include=[
    'celery_task.sms_task'
])

# 时区
work.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
work.conf.enable_utc = False

# 任务的定时配置
work.conf.beat_schedule = {
    'low-task': {
        'task': 'celery_task.tasks.low',
        'schedule': timedelta(seconds=3),
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (300, 150),
    }
}
