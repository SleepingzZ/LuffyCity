from rest_framework import serializers

from ..models import CourseCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id', 'name']
