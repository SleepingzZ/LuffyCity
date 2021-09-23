from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInfo(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, null=True)
    icon = models.ImageField(upload_to='icon', default='icon/default.png')

    class Meta:
        db_table = 'LuffyCity'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
