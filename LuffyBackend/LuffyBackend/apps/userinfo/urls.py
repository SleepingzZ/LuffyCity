from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LoginView, CheckMobileView

router = SimpleRouter()
router.register('', LoginView, 'login')
router.register('', CheckMobileView, 'mobile')
urlpatterns = [
    path('', include(router.urls)),  # 自动生成路由需要配置 action 装饰器
    # path('login', LoginView.as_view({'post': 'login'})),  # 不需要 action 装饰器
]