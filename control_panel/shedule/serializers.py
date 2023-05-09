from rest_framework import serializers


from .models import Lesson, LessonDate
from personnel.models import User as Teacher


class LessonDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDate
        fields = ['date']

       
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name']


class LessonSerializer(serializers.ModelSerializer):
    lesson_type = serializers.CharField(source='type_name', read_only=True)
    lesson_time = serializers.CharField(source='academic_couple', read_only=True)
    teacher = TeacherSerializer(many=True)
    
    lesson_date = LessonDateSerializer(read_only=True, many=True)
    
    class Meta:
        model = Lesson
        fields = ['id', 'lesson_date', 'lesson_time', 'week', 'lesson_type', 'auditorium', 'teacher']