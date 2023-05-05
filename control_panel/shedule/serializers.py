from rest_framework import serializers

from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['pk', 'week', 'type_name', 'auditorium']

class LessonGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['pk', 'lesson_id', 'group_id']
        
class LessonSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['pk', 'lesson_id', 'subject_id']