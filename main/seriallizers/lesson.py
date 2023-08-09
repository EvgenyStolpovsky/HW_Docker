from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from main.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор представление модели Lesson"""


    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'course', 'user']
