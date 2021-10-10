from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from django.conf import settings
from .models import BannerModel
from .serializer.banner import BannerSerializer
from django.core.cache import cache
from rest_framework.response import Response

# Create your views here.


class BannerView(GenericViewSet, ListModelMixin):
    queryset = BannerModel.objects.all().filter(
        is_delete=False, is_show=True).order_by('orders')[:settings.BANNER_COUNT]
    serializer_class = BannerSerializer


