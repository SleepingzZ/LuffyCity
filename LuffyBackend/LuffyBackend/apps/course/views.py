from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from utils.paging import CustomPagination
from .models import CourseCategory, Course
from .serializer.course_category import CategorySerializer
from .serializer.courses import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CourseView(GenericViewSet, ListModelMixin):
    queryset = Course.objects.all().filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = CourseSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    pagination_class = CustomPagination  # 分页功能
    ordering_fields = ['id', 'students', 'price']  # 排序功能: 按 id、学生数量或价格排序
    filter_fields = ['course_category']  # 过滤功能: 按课程分类


class CourseCategoryView(GenericViewSet, ListModelMixin):
    queryset = CourseCategory.objects.all().filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = CategorySerializer



