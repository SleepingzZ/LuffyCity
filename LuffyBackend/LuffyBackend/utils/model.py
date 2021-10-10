from django.db import models


class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_show = models.BooleanField(default=True, verbose_name='是否显示')
    orders = models.IntegerField(verbose_name='优先级')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        abstract = True  # 仅用于继承


