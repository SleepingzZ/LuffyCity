from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CourseCategoryView, CourseView

router = SimpleRouter()
router.register('actual', CourseView)  # 获取所有课程
router.register('categories', CourseCategoryView)  # 获取课程分类

urlpatterns = [
    path('', include(router.urls)),
]
