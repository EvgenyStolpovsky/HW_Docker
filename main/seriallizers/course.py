from rest_framework import serializers


from main.models import Course, Lesson
from main.seriallizers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор представление модели Course"""

    class Meta:
        model = Course
        fields = ['name', 'description', 'lessons', 'lessons_count']
