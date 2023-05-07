from rest_framework import serializers


from .models import Lesson, LessonDate
from students.serializers import GroupSerializer


class LessonDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDate
        fields = ['date']


class LessonSerializer(serializers.ModelSerializer):
    lesson_type = serializers.CharField(source='type_name', read_only=True)
    lesson_time = serializers.CharField(source='academic_couple', read_only=True)
    
    group = GroupSerializer(read_only=True, many=True)
    lesson_date = LessonDateSerializer(read_only=True, many=True)
    
    class Meta:
        model = Lesson
        fields = ['lesson_date', 'lesson_time', 'week', 'lesson_type', 'auditorium', 'group']