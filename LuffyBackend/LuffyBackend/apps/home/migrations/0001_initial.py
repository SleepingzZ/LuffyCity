# Generated by Django 2.2.2 on 2021-09-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(verbose_name='优先级')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('info', models.TextField(max_length=64, verbose_name='详情')),
                ('link', models.CharField(max_length=64, verbose_name='链接')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'db_table': 'Luffy_Banner',
            },
        ),
    ]
