from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import BannerView

router = SimpleRouter()
router.register('banner', BannerView)
urlpatterns = [
    path('', include(router.urls)),
]
