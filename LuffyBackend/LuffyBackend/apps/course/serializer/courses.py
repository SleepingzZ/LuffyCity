from rest_framework import serializers
from .teacher import TeacherSerializer
from ..models import Course


class CourseSerializer(serializers.ModelSerializer):
    # ε­εΊεε
    teacher = TeacherSerializer()

    class Meta:
        model = Course
        fields = ['id', 'name', 'students', 'teacher',
                  'sections', 'pub_sections', 'price', 'course_section_list', 'course_img']
