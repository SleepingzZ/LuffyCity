from rest_framework import serializers
from home.models import BannerModel


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = ['title', 'image', 'info', 'link']
