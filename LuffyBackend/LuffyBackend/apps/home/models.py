from django.db import models

from utils.model import BaseModel


# Create your models here.


class BannerModel(BaseModel):
    title = models.CharField(max_length=32, unique=True, verbose_name='标题')
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    info = models.TextField(max_length=64, verbose_name='详情')
    link = models.CharField(max_length=64, verbose_name='链接')

    class Meta:
        db_table = 'Luffy_Banner'
        verbose_name_plural = '轮播图'

    def __str__(self):
        return self.title
